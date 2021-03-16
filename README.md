# TSSC
Testarea Securitatii Sistemelor de Calcul - UPB 2021:
https://ocw.cs.pub.ro/courses/isc


## Laboratoare
### Laborator 1
Chestii introductive, oarecum recapitulative. Nimic complicat, doar cerinta 8
e prea tractor si prea jegoasa.

### Laborator 2
Se folosesc cateva functii din API-ul **SGX**:
- `sgx_read_rand`
- `sgx_seal_data`
- `sgx_unseal_data`
pentru a se cripta un mesaj random, care apoi este scris intr-un fisier, citit
si decriptat.
