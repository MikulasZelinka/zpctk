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

Sinus formule (s počáteční hodnotou 3):

![](http://latex.codecogs.com/gif.latex?a_%7Bn%7D%20%3D%20a_%7Bn-1%7D%20&plus;%20sin%28a_%7Bn-1%7D%29%20%5Crightarrow%20%5Cpi)

Basel formule:

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7B1%5E2%7D%20&plus;%20%5Cfrac%7B1%7D%7B2%5E2%7D%20&plus;%20%5Cfrac%7B1%7D%7B3%5E2%7D%20&plus;%20...%20%3D%20%5Cfrac%7B%5Cpi%5E2%7D%7B6%7D)
