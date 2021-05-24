# TSSC
Testarea Securitatii Sistemelor de Calcul - UPB 2021:
https://ocw.cs.pub.ro/courses/isc


## Laboratoare
### Laborator 1 - Generalitati
Chestii introductive, oarecum recapitulative. Nimic complicat, doar cerinta 8
e prea tractor si prea jegoasa.

### Laborator 2 - Securitate Hardware (SGX)
Se folosesc cateva functii din API-ul **SGX**:
- `sgx_read_rand`
- `sgx_seal_data`
- `sgx_unseal_data`
pentru a se cripta un mesaj random, care apoi este scris intr-un fisier, citit
si decriptat.

### Laborator 3 - Criptografie
Se experimenteaza metode de decriptarea a *AES*, *RSA*, *OTP* etc folosind
diverse informatii fie despre cheii, fie despre mesajele transmise.

### Laborator 4 - Controlul accesului
Facut doar pe fep pentru ca era nevoie de creat utilizatori, grupuri, basini.
Se folosesc perimisiuni (printre care si SETUID si SETGIT) + ACL-uri ca sa se
gestioneze accesul unor utilizatori la diverse directoare si fisiere.

### Laborator 5 - Application Security
Se face un buffer overflow chior prin care se apeleaza o functie cu un parametru
suprascriind EIP-ul.

### Laborator 6 - OS Security
Se apeleaza un shellcode si se creeaza un mic DOS pentru un server de apache2
care ruleaza **intr-un container de docker in plm...**. Interesant e ca serverul
omoara conexiunea catre scriptul care ruleaza exploitul dupa ceva timp de cand
i se umple memoria, deci nu-i chiar asa prost.

### Laborator 7 - Network Security
Rahaturi cu `iptables` si un atac *Man in the Middle*. Toate atacurile se fac pe
dockere. Cam plictisitor labul asta.

### Laborator 8 - Web Security
In sfarsit un lab mai ok ca se fac atacuri de*SQL Injection*. In rest tot
mizerii. Si, bineinteles, labul explicat ca un cur.

### Laborator 9 - Forensics
CTF-uri pe teme generice, de obicei fisiere cu diverse formate. Printre cele mai
misto laburi.

## Laborator 10 - PGP
Comenzi simple de *GPG*: creare, semnare de chei, criptare si semnare de mesaje,
precum si decriptare si verificare semnaturi. Facut pe *OpenStack*.

## Laborator 11 - ML Security
Se foloseste un *ResNet 18* pentru a genera un input care sa fie clasificat
drept semnul rutier *STOP*. Un lab usurel, si clar mai interesant decat ala de
GPG.


## Teme
### Tema 1
Tema contine 3 cerinte: o mizerie de cripto care pana la urma a fost relativ
interesanta, un exploit foarte misto al `SETUID` si un buffer overflow banal, ca
la IOCLA.
