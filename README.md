# Různé metody výpočtu π
## Cíl
Cílem tohoto programu je porovnat různé metody výpočtu π na základě času běhu programu.

## Závislosti
matplotlib

##  Použití
Program se spouští spuštěním main.py. Ovládá se příkazy z konzole. Nabízí možnosti vygenerování dat (runtimů
metod), vykreslení výsledků do grafů a vizualizaci metody Monte Carlo.
![alt text](https://github.com/bhonza/zpctk/blob/master/pictures/picture1.png)
![alt text](https://github.com/bhonza/zpctk/blob/master/pictures/picture2.png)
![alt text](https://github.com/bhonza/zpctk/blob/master/pictures/picture3.png)


## Využité metody
Monte Carlo - https://en.wikipedia.org/wiki/Monte_Carlo_method

Leibnitzova formule: 4 - 4/3 + 4/5 - 4/7 + 4/9 - ... = pi

Sinus formule: a_(n) = a_(n-1) + sin(a_(n-1)) pro počáteční hodnotu 3 -> π

Basel formule: 1/(1^2) + 1/(2^2) + 1/(3^2) + ... = (π^2)/6
