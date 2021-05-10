# Laborator 9 - Forensics
... adica un CTF cu teme diverse, necorelate cu web/binaries.

## 0. Wireshark
```
PASS ISC{sending_passwords_in_cleartext_is_not_smart}
```
Am filtrat in *Wireshark* ca sa vad doar pachetele *TCP*, iar la final era
un schimb de mesaje prin *FTP*, in care raspunsul continea flagul.


## 1. Fisier comprimat cu gunzip
```
ISC{file_is_our_friend}
```
Pentru a vedea ce e cu fisierul `01-File` am rulat comanda `file` pe el, care
spunea ca e o arhiva **gzip**. Asadar, am adaugat extensia `.gz` fisierului si
am rulat `gunzip` pe el, rezultand un fisier text ce continea flagul de mai sus.


## 2. Imagine PNG
```
ISC{we_all_love_grep}
```
Eu n-am folosit *grep*, ci [vim](https://xkcd.com/378/) (/jk. nu folosesc vim de
obicei :))) ). Am cautat sirul "ISC" si am gasit flagul.


## 3. Imagine JPG
```
ISC{no_more_ideas_for_flags}
```
Am deschis imaginea tot in **vim** si am comparat headerul cu cel de pe
[wikipedia](https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format#File_format_structure).
Am vazut ca primii 2 octeti trebuie sa fie `ff d8`, dar in imagine ei erau
`ee d9`, asa ca i-am corectat, dupa care am deschis imaginea si am citit flagul.


## 4. Audio
```
ISC{spectogram_for_the_win}
```
Exercitiul asta chiar e misto. Pacat ca a trebuit sa instalez toate cacaturile
(audacity, wxWidgets...) pentru el. Flagul e insasi spectograma fisierului
`.wav`.


## 5. Fisier ascuns
```
ISC{fileception_is_real}
```
Aici am rulat `binwalk -e` pe poza si am vazut ca ea contine si o arhiva `.7z`
la offsetul 33519. Am extras arhiva folosind comanda:
```
dd if=05-Idea.jpg of=flag.7z ibs=1 skip=33519
```
dupa care am dezarhivat `flag.7z` pe [acest site](https://extract.me/), iar in
poza rezultata era flagul.


## 6. PDF
```
ISC{hidden_in_the_dark}
```
Am cautat pe net cum sa editez pdf-uri si dupa ce n-am gasit mai nimic util, in
afara de sugestii de a-l converti in alte formate. Am incercat word, ppt si alte
cateva, dar n-au mers. Ceea ce a mers a fost sa-l convertesc la *HTML* folosind
site-ul [asta](https://pdf.online/convert-pdf-to-html). In imaginea *HTML*
aparea flagul fara bara neagra de deasupra.


## 7. GIF
```
ISC{what_were_you_waiting_for}
```
Foarte tare asta! Am spart gif-ul in cadre pe site-ul
[asta](https://ezgif.com/split/ezgif-1-fd1ffb302d59.gif), dupa care am scanat
codul QR si am obtinut flagul.


## 8.GIF
```
ISC{keycap}
```
Si asta a fost interesant. Nu stiam cum sa interpretez `.pcap`-ul in wireshark,
asa ca am cautat pe net si am gasit writeupul
[asta](https://blog.stayontarget.org/2019/03/decoding-mixed-case-usb-keystrokes-from.html), care explica felul in care pot sa extrag tastele apaste:
```
tshark -r 08-Capture\ 2.pcap -T fields -e usb.capdata > flag.usb.txt
```
Apoi, folosind scriptul din writeup rulat pe `flag.usb.txt` am obtinut flagul.
