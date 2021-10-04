# Cifru OTP care foloseste repetat aceeasi cheie
Se dau 10 cifruri criptate cu aceeasi cheie is trebuie decriptat un al XI-lea
cifru, criptat tot cu cheia folosita si pentru celelalte.

Decriptarea se bazeaza pe 2 observatii:
- `c1 ^ c2 = m1 ^ k ^ m2 ^ k = m1 ^ m2`
- in _ASCII_, diferenta dintre literele mici si cele mari e de 32 (0x20,
caracterul `' '`)

Se xoreaza cifrul care trebuie decriptat cu celelalte 10. Pe baza observatiilor
de mai sus, orice spatiu din cele 10 mesaje o sa expuna o litera din mesajul
tinta (literele mari o sa apara mici si invers), iar orice spatiu din mesajul
care trebuie aflat, o sa produca o litera in aproape toate celelalte mesaje
(exceptie facand semnele de punctuatie sau alte spatii).

Se afiseaza rezultatele operatiilor de mai sus si pe baza lor se compune
mesajul cerut, care, apoi, se prelucreaza manual, ochiometric, ca sa se
corecteze erorile aparute si imprecizia metodei de descifrare. Rezultatul
xorarii e urmatorul:
```c
--EC--C---T--S---EN--XE-HT------GQ-A----A-O--------N--E-A-S-L--EF---O-O--ET---B--CT
---E-E----DM------L-S-N---NT---N-O-----E--E----E-IC----RAU--R-------N-O-------T-NNE
--------E-H---S---U-SqE----QU--N-O----R---P------DE--V--NU--I--EAK--TM--EF---------
----------T---S---D---Dw--NAU------N------O-I-----I---E-O------EG------R-I----T---E
-------U-TW---S--EB---Aw------I--RAK---E--O-I-H--U----E-P---A---E-E-NM---A---------
---R-E---TT--S----SI-------T-----H---T----------R-I--V--E-S-E---T-E-A--R-R--A-O--C-
---R-E---TT--S----SI-------O-----Y-----E--A-I-----SN---Rg---R---N-E-OM--------EO---
--EC--C-------S---N-SMH---NT--I--I----R---A---H---AN----GU--TT------TM--------U---E
-HMP----------ZAG-N--CP----------EAS-----M-C-----ET---IRN---L-H-----C----ET--------
t--ES-----S-E-----D--YT----R-SA-W-W-S-----N--P----T-E--RT--EA--EO-EYW----N-H-NRO---
```

Din el, se poate deduce mesajul cerut:
```c
The secret message is: When using a stream cipher, never use the key more than once
```
