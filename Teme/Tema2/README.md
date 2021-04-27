# Tema 2 TSSC - Securitate Web
## Cerinta 1
```
SpeishFlag{JdYwzaWeoObO84QKtMl93jWMsRPKx8UV}
```
Doar am deschis `traffic.pcap` in *Wireshark* si am cautat prin raspunsurile
primite de la server pana am gasit cheia privata, cu care m-am logat prin *SSH*
la endpointul din enunt:
```bash
teo@obor task1 $ ssh -i id_rsa secure@isc2021.root.sx
You did it! Congratulations!

Your flag is:

SpeishFlag{JdYwzaWeoObO84QKtMl93jWMsRPKx8UV}

Connection to isc2021.root.sx closed.
```


## Cerinta 2
### Primul flag
```
SpeishFlag{xesOb3jmqp2o99u5R3X0E8jMLse9WNZn}
```

Am observat ca butonul de `register` ma duce spre calea `/auth/fake_login`, asa
ca m-am uitat in codul sursa *HTML* al paginii, unde am gasit un comentariu
catre likul real de login: `/auth/register_real_one`. Mi-am facut cont, m-am
logat cu el si m-am uitat din nou in codul sursa al paginii, de data aceasta in
cel al caii: `/inside`, unde am gasit flagul.


### Al doilea flag
```
SpeishFlag{bwZjYXYnJ0f8ucN8yoGB3KF6t7AFtHnQ}
```

Initial, am incercat sa-i dau *friend request* bossului. Degeaba. Iar m-am uitat
in codul site-ului si apoi in `main.js` si am observat ca e destul da apele eu,
de pe profilul meu, `acceptFriend(boss_id)` ca bossul sa imi accepte si el
cererea. Am incercat sa apelez `acceptFriend(theboss)` si n-a mers. Asa ca am
sperat ca poate id-urile ar putea fi ca intr-o baza de date. Am incercat 0 si 1,
iar 1 a mers, iar pe profilul bossului am gasit flagul.


### Al treilea flag
```
SpeishFlag{FPFcPKwWeeDvGNGsl281MYyT5vU1W3t3}
```

Pe wallul bossului am gasit scriptul `backup.sh`, cu care serverul arhiveaza
directorul curent (inca nu se stie care e) in fisierul `backup-orig.tar.gz`. De
asemenea, scriptul arhiveaza si /fisierul `flag.txt` in `/tmp/flag.tar.gz`, iar
la final concateneaza aceste 2 arhive in fisierul
`backup-<data curenta>.tar.gz`.

Dar nu stiam unde e `backup.sh` (probabil `backup-<data curenta>.tar.gz` e in
acelasi director), asa ca am descarcat intregul director de la `localhost:8080`,
prin `wget`, folosind cookie-urile luate din browser, pentru a pastra
autentificarea la server:
```
wget -r http://localhost:8080/ --load-cookies cookies
```
Uitandu-ma prin directoarele serverului, am vazut ca `backup.sh` se afla in
radacina, deci probabil si `backup-<data curenta>.tar.gz` e in acelasi loc. Ca
sa ghicesc data, am facut scriptul `bruteforce_dates.sh` in care am luat la rand
datele din secolul al XXI-lea si am incercat sa dau `curl` la
```
curl -b cookies -f --silent --output backup.tar.gz http://localhost:8080/backup-<data>.tar.gz
```
pana am gasit data buna, care e `2021-04-11`. Am cautat apoi unde incepe arhiva
cu flagul. Headerul unui fisier `.tar.gz` incepe cu `0x1f 0x8b 0x08`. Am gasit
3 indecsi in binar la care se gasesc cei 3 octeti enumerati anterior. Primul e 0
(duh...), al 2-lea e intamplator, iar al 3-lea e headerul legit, la indexul
`0x381dcf`.

Ce a urmat a fost sa extrag ultima parte a fisierului, de la indexul gasit:
```
tail -c +$((16#381dd0)) backup.tar.gz > flag.tar.gz
```
iar in fisierul `flag.txt` rezultat din dezarhivarea arhivei `flag.tar.gz`, se
gaseste flagul.
