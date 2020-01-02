import random as rng
import math
import numpy as np
import matplotlib.pyplot as plt
import methods
import time
import os

'''
   toto je hlavni cast programu
   zavolani testovani vsech metod, zapsani jejich vysledku do souboru a posleze vypsani
   program se bude ovladat z konzole
   vse bude bezet, dokud uzivatel nezada 'exit'
'''

pocetIteraci = 0

def uvod():
    global pocetIteraci
    print('Tento program porovnava iterativni metody approximace pi na zaklade poctu iteraci')
    print()
    print('Porovnavame nasledujici metody: MonteCarlo, Archimedes(polygon), Gregory-Leibniz, Machin, Gauss')
    print()
    pocetIteraci = int(input('Zadejte pocet iteraci pro otestovani kazde metody (pro preskoceni testovani zadejte 0): '))
    if pocetIteraci > 0:
        print('Vysledky budou v souboru: ', pocetIteraci, '.txt', sep='')
    else:
        print('Preskakuji testovani')


def zobraz():
    ls = os.listdir()
    print(ls)
    soubor = input('Zadejte nazev souboru z ktereho chcete zobrazit data: ')
    # vezme data ze souboru a graficky je zobrazi
    # zaroven zobrazi vizualizaci metody monte carlo
    pass

def zapis(method, runtime, value):
    global pocetIteraci
    f = open(f'{pocetIteraci}.txt', 'wb') 
    f.write(method, runtime, value, sep='\n')
    f.close()

def otestuj(pocetIteraci):
    # otestuje vsechny metody se zadanym poctem iteraci 
    pass

if pocetIteraci > 0:
    otestuj(pocetIteraci)
    # zapis to co funkce vraci do souboru (nazev metody, runtime: , aproximovana hodnota)

else:
    pass
 
# tohle bude loop programu
end = False
while end == False:
    odpoved = 0
    end = True 
    pass


