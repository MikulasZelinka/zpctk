import methods # methods.py --- testovane metody
import view # view.py --- zobrazeni

import random as rng
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import os

'''
   toto je hlavni cast programu
   zavolani testovani vsech metod, zapsani jejich vysledku do souboru a posleze vypsani
   program se bude ovladat z konzole
   vse bude bezet, dokud uzivatel nezada 'exit'
'''
ref = math.pi # referencni hodnota pi
timeout = 0
precision = 0

def uvod():
    global precision
    print('Tento program porovnava iterativni metody approximace pi na zaklade poctu desetinnych mist a casu behu programu')
    print()
    print('Porovnavame nasledujici metody: MonteCarlo, Archimedes(polygon), Gregory-Leibniz, Machin, Gauss')
    print()
    precision = int(input('Zadejte pozadovanou presnost (pro preskoceni testovani zadejte 0): '))
    if precision > 0:
        print('Vysledky budou v souboru: ', precision, '.txt', sep='')
    else:
        print('Preskakuji testovani')

def zapis(method, runtime):
    global precision
    f = open(f'{precision}.txt', 'wb') 
    f.write(method, runtime, value, sep='\n')
    f.close()

def otestuj(precision):
    # otestuje vsechny metody se zadanym poctem iteraci 
    pass

if precision > 0:
    otestuj(precision)
        # zapis to co funkce vraci do souboru (runtimes pro zadanou metodu)
else:
    view.zobraz()
 
# tohle bude hlavni smycka programu
end = False
while end == False:
    odpoved = 0
    end = True 
    pass


