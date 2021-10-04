# Cripto
[Introducere in Criptologie - UPB 2019-2020](https://ocw.cs.pub.ro/courses/ic)\
[Appliced Cryptography - UPB 2020-2021](https://ocw.cs.pub.ro/courses/ac)\
[Criptography I - Coursera](https://www.coursera.org/learn/crypto)

## Laboratoare
### IC
#### 1. Introducere in Python
- _Shift Cipher_
- _OTP_
- Conversii intre tipuri de date _Python_: `str` (_ASCII_, hex, binar), `bytes`

#### 2. Cifruri Shift + Vigenere
- **Ex. 1:** Decriptarea unor cifruri criptate folosind un _shift cipher_
- **Ex. 2 + 3:** Decriptarea unor cifruri prin substitutie prin analiza
frecventelor literelor si a grupurilor de 2 litere
- **Ex. 4:** Modificarea unui cifru _OTP_ pentru a altera mesajul incifrat

#### 3. PRG
- **Ex. 1:** Spargerea unui PRG ce foloseste un generator liniar
- **Ex. 3:** Implementarea testului
[monobit](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf#%5B%7B%22num%22%3A141%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D)
pentru a verifica daca un PRG e sau nu random. Se testeaza cel de la _ex. 1_ si
unul generat aleator

#### 4. PRF + PRP
- **Ex. 2:** Se sparge o retea de substitutii si permutari care efectueaza o
singura operatie de `XOR` cu cheia, la inceput
- **Ex. 3:** Se sparge o retea de substitutii si permutari care `XOR`-eaza
inputul cu chei atat inainte, cat si dupa ce face substitutii si permutari

#### 5. DES
Se demonstreaza de ce _2DES_ nu e un algoritm sigur. Pentru aceasta, se
foloseste un atac _meet-in-the-middle_ prin care se determina cele 2 chei
folosite de _2DES_.

#### 8. MAC-uri
Se implementeaza un atac de tipul paradoxului zilelor de nastere: pentru a se
gasi o coliziune la nivelul primelor 4 octeti ai hash-urilor unor mesaje, se
genereaza grupuri `sqrt(1 << 32) = 1 << 16` mesaje caora li se calculeaza
hash-urile. Atunci cand se gaseste o coliziune, generarea se opreste.


### AC
#### 1. Introducere in Python
Fata de [Labul 1 de IC](#1-introducere-in-python), e aceeasi Marie cu alta
palarie.


### Coursera
#### 1. Cifruri pe fluxuri
- _OTP_
- _PRG_
- Securitate semantica

#### 2. Cifruri bloc
Decriptarea unui cifru AES in modurile _CBC_ si _CTR_.

#### 3. Hash rezistent la coliziuni
Se calculeaza hashul unui videoclip pe sectiuni de `1kB`. Acesta se imparte in
blocuri de `1kB` si porneste de la ultimul, iar la fiecare pas se calculeaza
hashul blocului curent, adica `SHA256(bloc_precedent + hash_precedent)`.
Ultimul hash calculat este hashul intregului fisier.

## Tema
