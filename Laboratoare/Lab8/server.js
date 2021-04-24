/**
 * Module dependencies.
 */

var express = require('express'),
  bodyParser = require('body-parser'),
  path = require('path'),
  session = require('express-session'),
  mysql = require('mysql');

var app = module.exports = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

var db = mysql.createConnection({
  host     : 'mysql',
  user     : 'guest',
  password : 'secretguest123',
  database : 'guestbook'
});
db.connect(runServer);

app.use(bodyParser.urlencoded({ extended: false }));
app.use(session({
  resave: false, // don't save session if unmodified
  saveUninitialized: false, // don't create session until something stored
  secret: 'mysecret123'
}));

// Session-persisted message middleware

app.use(function(req, res, next){
  var err = req.session.error;
  var msg = req.session.success;
  delete req.session.error;
  delete req.session.success;
  res.locals.message = '';
  if (err) res.locals.message = '<p class="msg error">' + err + '</p>';
  if (msg) res.locals.message = '<p class="msg success">' + msg + '</p>';
  next();
});

// Authenticate using our plain-object database of doom!

function authenticate(name, pass, fn) {
  console.log('authenticating %s:%s', name, pass);
  // query the db for the given username and password
  db.query("SELECT * FROM `users` WHERE name='" + name + "' AND password='" + pass + "' LIMIT 1",
    function(error, results, fields) {
      if (error) {
        fn(error);
      } else if (results.length) {
        fn(null, results[0]);
      } else {
        fn(new Error('invalid username or password!'));
      }
    });
}

function get_entries(fn) {
  db.query('SELECT * FROM `entries` LEFT JOIN `users` ON `users`.`id`=`entries`.`user_id` ORDER BY `date` ASC',
    function(error, results, fields) {
      if (error) {
        fn(error);
      } else {
        fn(null, results)
      }
    });
}

function restrict(req, res, next) {
  if (req.session.user) {
    next();
  } else {
    req.session.error = 'Access denied!';
    res.redirect('/login');
  }
}

app.get('/', function(req, res){
  if (req.session.user) {
    res.redirect('/guestbook');
  } else {
    res.redirect('/login');
  }
});

app.get('/logout', function(req, res){
  // destroy the user's session to log them out
  req.session.destroy(function(){
    res.redirect('/');
  });
});
app.get('/login', function(req, res){
  res.render('login');
});

app.post('/login', function(req, res){
  authenticate(req.body.username, req.body.password, function(err, user){
    if (user) {
      req.session.regenerate(function(){
        req.session.user = user;
        res.redirect('/guestbook');
      });
    } else {
      req.session.error = 'Authentication failed: ' + err;
      res.redirect('/login');
    }
  });
});

app.get('/guestbook', restrict, function(req, res){
  get_entries(function(err, entries) {
    res.locals.user = req.session.user;
    res.locals.entries = []
    if (err) {
      req.session.error = "Query failed: " + err;
    } else {
      res.locals.entries = entries;
    }
    res.render('guestbook');
  });
});

app.post('/guestbook/post', function(req, res) {
  var query = "INSERT INTO `entries` (`date`, user_id, message) VALUES (NOW(), " +
    req.session.user.id + ", " + db.escape(req.body.message) + ")";
  db.query(query,
    function(error, results, fields) {
      if (error) {
        req.session.error = "Query failed: " + error;
      }
      res.redirect('/guestbook');
    });
})

app.use(express.static(__dirname));

function runServer(error) {
  if (error) {
    console.error('Error connecting to MySQL database: ' + error.stack);
    console.log('Please try again!');
    return;
  }
  app.listen(8080);
  console.log('NodeJS Express started on port 8080');
}

process.on('SIGINT', function() {
  console.log("Caught interrupt signal, quitting...");
  process.exit();
});

