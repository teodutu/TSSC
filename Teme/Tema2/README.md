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
Am observat ca butonul de `register` ma duce spre calea `/auth/fake_login`, asa
ca m-am uitat in codul sursa *HTML* al paginii, unde am gasit un comentariu
catre likul real de login: `/auth/register_real_one`. Mi-am facut cont, m-am
logat cu el si m-am uitat din nou in codul sursa al paginii, de data aceasta in
cel al caii: `/inside`, unde am gasit flagul:
```
SpeishFlag{xesOb3jmqp2o99u5R3X0E8jMLse9WNZn}
```

### Al doilea flag
Initial, am incercat sa-i dau *friend request* bossului. Degeaba. Iar m-am uitat
in codul site-ului si apoi in `main.js` si am observat ca e destul da apele eu,
de pe profilul meu, `acceptFriend(boss_id)` ca bossul sa imi accepte si el
cererea. Am incercat sa apelez `acceptFriend(theboss)` si n-a mers. Asa ca am
sperat ca poate id-urile ar putea fi ca intr-o baza de date. Am incercat 0 si 1,
iar 1 a mers, iar pe profilul bossului am gasit flagul:
```
SpeishFlag{bwZjYXYnJ0f8ucN8yoGB3KF6t7AFtHnQ}
```
