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

### Laborator 5 - Application security
Se face un buffer overflow chior prin care se apeleaza o functie cu un parametru
suprascriind EIP-ul.

### Laborator 6 - OS Security
Se apeleaza un shellcode si se creeaza un mic DOS pentru un server de apache2
care ruleaza **intr-un container de docker in plm...**. Interesant e ca serverul
omoara conexiunea catre scriptul care ruleaza exploitul dupa ceva timp de cand
i se umple memoria, deci nu-i chiar asa prost.
