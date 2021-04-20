# Tema 1 - TSSC
**Username:** teodor_stefan.dutu

## Task 1
**Flag:** `SpeishFlag{HRSR533Gkji0T8fCOYJtXSmPfoVY7dNk}`

Uitandu-ma in functia `keystream` din `cryptolocker.py` am observat ca se
porneste de la octetul 67 pentru a se crea cheia pentru stream cipher. Mai
mult, dat fiind algoritmul de generare a cheii, mi-am dat seama ca aceasta
va fi periodica si va cicla dupa `2 * len(key)` pasi. Asadar, era suficient sa
descopar primii maximum 22 (dat fiind ca lungimea cheii nu poate fi mai mare de
11 caractere) de octeti din keystream, pentru ca restul sunt replicari ale
acestora.

In acest sens, am aplicat operaia `XOR` intre datele din fisiere si `67`, ceea
ce a dezvaluit cateva litere din textele originale, la pozitiile la care cheia
s-ar fi resetat. Am dedus din aceste fragmente ilustrele opere "Dau cu zaru' 6
5" si "Ti-am luat 7 trandafiri" de Florin ~~Salam~~ Stoian, precum si "Plumb" de
Bacovia. Celelalte poezii ("Ninge" si "Noapte") nu le-am recunoscut, dar nu-s
nici cele mai reusite ale autorului... Recomand "Palind", "Ego" si, pentru anul
4, "Gaudeamus".

Revenind, Folosind primele versuri din "Dau cu zaru' 6 5" xorate cu datele
originale din fisierul cu manele, am obtinut partea unica a cheii:
```
!,*+:qq)3CCCCCCCCC
```
De remarcat ca aceasta se reseteaza, caci codul `ASCII` al caracterului 'C' este
67.

Acum, folosind cheia, am decriptat toate fisierele.


## Task 2
**Flag:** `SpeishFlag{NbqBQWNKThSCH5NQ4CUOTMSQEIJx6wuM}`

Initial am cautat folosind `find` fisierul cu flagul. Am gasit
`/usr/bin/something/here/flag-2019`. Am incercat sa dau in el cu ce am putut,
dar n-aveam permisiuni sa fac nimic. Un singur user avea: `mishelu`. Am cautat
apoi, tot cu `find`, ceva "hints" si le-am gasit in
`/etc/opt/something/here.bin`, impreuna cu un binar, `aaaaaaaa` ce avea
`SETUID` activat si apartinea tot userului `mishelu`, deci puteam sa-l folosesc
ca sa citesc flagul.

Dupa ce am sapat prin binarul asta cu `objdump`, am inteles ca vrea un string
ca parametru, pe care-l compara cu `de9ba2b0ad0b02c3dae744e3a16cd7e0`. Daca
stringurile erau identice, binarul executa
`system("file /usr/bin/something/here/flag-2019")`. Numele fisierului e copiat
intr-un buffer cu `snprintf`, dar asta nu e relevant pentru ca nu puteam ataca
binarul.

Ce puteam face si am si facut a fost sa-l pacalesc si sa-i dau alta comanda
in loc de `file`. In acest sens, am creat un nou "executabil" `file` in `/tmp`,
unde orice user are drept de executie, in care am scris comanda de care aveam
nevoie pentru a citi flagul: `cat /usr/bin/something/here/flag-2019`. Apoi, am
dat drept de executie noului executabil si am modificat variabila de mediu
`PATH` astfel incat `file` sa fie cautat mai intai in `/tmp` pentru a inlocui
adevaratul binar `file`. Nu in ultimul rand, am rulat binarul `aaaaaaaa` in
noile conditii si am obtinut flagul, dupa cum se poate vedea mai jos:
```bash
parlit@fhunt:/etc/opt/something/here.bin$ ./aaaaaaaa de9ba2b0ad0b02c3dae744e3a16cd7e0
/usr/bin/something/here/flag-2019: ASCII text
parlit@fhunt:/etc/opt/something/here.bin$ cd /tmp
parlit@fhunt:/tmp$ echo "cat /usr/bin/something/here/flag-2019" > file
parlit@fhunt:/tmp$ chmod 777 file 
parlit@fhunt:/tmp$ export PATH=/tmp:$PATH
parlit@fhunt:/tmp$ cd -
/etc/opt/something/here.bin
parlit@fhunt:/etc/opt/something/here.bin$ ./aaaaaaaa de9ba2b0ad0b02c3dae744e3a16
cd7e0
SpeishFlag{NbqBQWNKThSCH5NQ4CUOTMSQEIJx6wuM}
```


## Task 3
**Flag:** `SpeishFlag{kDaeHPXthCkxhnHmnfD2ppgOGKQSNZtW}`

Aici am deschis binarul `casino` in `ghidra`, unde am vazut ca imediat dupa
intrarea in `main` se apeleaza `frnr66` care citeste de la `stdin` cu `gets`,
care e extrem de vulnerabila la buffer overflow, deoarece nu verifica
dimensiunea inputului. `memset`urile din jurul lui `gets` sunt doar la deruta,
nu incura la nimic.

Tot in `gidra` am observat functia `win`, care, daca i se da parametrul
`0x11333703`, citeste continutul flagului. Adresa functiei este `0x0804861b` si
atacul presupune un buffer overflow in functia `frnr66` pentru a suprascrie
`EIP`-ul salvat pe stiva si a continua executia din functia `win`.

Am vazut in `ghidra` ca `gets` citeste incepand de la adresa `EBP - 51`, deci,
pentru a ajunge la `EIP`, a fost nevoie de un padding de 51 + 4 (pentru a
suprascrie `EBP`-ul lui `main` salvat pe stiva) = 55 octeti. In payload urmeaza
adresa lui `win` scrisa little endian.

Este nevoie de setarea primului parameteru al lui `win` la `0x11333703`. Acesta
se va afla la 4 octeti "mai sus" (la o adresa mai mare) fata de `EIP`-ul
suprascris. Cei 4 octeti provin din preambului lui `win`, in care se salveaza pe
stiva vechiul `EBP`. Similar cu adresa lui `win`, am pus pe stiva numarul
dorit de functie in format little endian.

Apoi, am folosit payloadul pentru a obtine flagul:
```bash
teo@obor task3 $ python2.7 -c 'print "A" * 55 + "\x1b\x86\x04\x08" + "AAAA" + "\x03\x37\x33\x11"' > payload
teo@obor task3 $ cat payload | nc isc2021.root.sx 10003
Welcome to the Saint Tropez Virtual Casino!
Please enter your bank account:
https://www.youtube.com/watch?v=pOyK9qQpdyQ SpeishFlag{kDaeHPXthCkxhnHmnfD2ppgOGKQSNZtW}
```
