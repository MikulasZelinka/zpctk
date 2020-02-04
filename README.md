# Různé metody výpočtu π
## Cíl
Cílem tohoto programu je porovnat různé metody výpočtu π na základě času běhu programu.

## Závislosti
matplotlib

##  Použití
Program se spouští spuštěním main.py. Ovládá se příkazy z konzole. Nabízí možnosti vygenerování dat (runtimů
metod), vykreslení výsledků do grafů a vizualizaci metody Monte Carlo.

### Ovládání
![alt text](https://github.com/bhonza/zpctk/blob/master/pictures/picture1.png)
### Grafy
![alt text](https://github.com/bhonza/zpctk/blob/master/pictures/picture2.png)
### MonteCarlo
![alt text](https://github.com/bhonza/zpctk/blob/master/pictures/picture3.png)


## Využité metody
### test
Monte Carlo - https://en.wikipedia.org/wiki/Monte_Carlo_method

Leibnitzova formule:
![](http://latex.codecogs.com/gif.latex?4%20-%20%5Cfrac%7B4%7D%7B3%7D%20&plus;%20%5Cfrac%7B4%7D%7B5%7D%20-%20%5Cfrac%7B4%7D%7B7%7D%20&plus;%20%5Cfrac%7B4%7D%7B9%7D%20-%20...%20%3D%20%5Cpi)

Sinus formule: $a_(n) = a_(n-1) + sin(a_(n-1)) pro počáteční hodnotu 3 -> π$

Basel formule: $1/(1^2) + 1/(2^2) + 1/(3^2) + ... = (π^2)/6$
