# Laborator 1 - Introducere
Niste cerinte introductive super simple, in afara de prima care-i autista

## 1. B64 encoding
Flag: `FLAG{so_many_64s}`

Fisierul e criptat **de mai multe** ori (16) cu base 64... 


## 2. EXIF
Flag: `FLAG{Kung_Fury}`.
Doar se da `xxd` pe poza, iar flagul e in header.


## 3. Manchester...
Flag: `FLAG{any_Vimto_aficionado_here?}`

https://www.dcode.fr/manchester-code +
https://www.rapidtables.com/convert/number/binary-to-ascii.html go brrrrr


## 4. GIF corupt
Flag: `flag{g1f_or_j!L}`

Fisierul are antetul busit: `9a` in loc de `GIF89a`. Se editeaza cu `vim`, dupa
care se deruleaza *GIF*-ul cadru cu cadru si se decodifica mesajul din
*base64*. Macar aici merge *base64*...


## 5. De insatalat apache2 si links
duh...


## 6. Oneliner
Trebuie aflata dimensiunea directoarelor din `/usr/include` cu o adancime de
maximum 2 si trebuie sortate crescator in functie de dimensiunea asta.

```bash
find /usr/include -maxdepth 2 -type d | xargs du | sort -k1 -n
```


## 7. De compilat un cod C
Trebuie instalata `libcurl4-gnutls-dev` si linkat cu `-lcurl`.


## 8. Compilare statica
O mizerie. Cumva chiar chiar daca se foloseste parametrul `-static`, binarul
e tot dinamic :(.


## 9. Capturare de trafic cu `tcpdump`
Se caputreaza tot traficul de pe retea intr-un fisier, folosind comanda:
```bash
sudo tcpdump -i enp0s31f6 -Z teo -w traffic.log
```
data **pe un sistem `ext`, nu `ntfs`!**
