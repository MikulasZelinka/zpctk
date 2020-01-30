import methods      # methods.py    <---> testovane metody
import view         # view.py       <---> zobrazeni
import time
import os
import math

'''
   toto je hlavni cast programu
   zavolani testovani vsech metod, zapsani jejich vysledku do souboru a posleze vypsani
   program se bude ovladat z konzole
   vse bude bezet, dokud uzivatel nezada 'exit'
'''

ref = math.pi # referencni hodnota pi
timeout = 5 # timeout pro testovani v s
precision = 8 # pocet desetinnych mist 
command = ""
data = [[], [], [], [], []]

print("Tento program porovnava iterativni metody approximace pi na zaklade casu behu programu")
print("---------------------------------------------------------------------------------------------------------------")
print("Porovnavame nasledujici metody: MonteCarlo, Archimedes(polygon), Gregory-Leibniz, Machin, Gauss")
print("---------------------------------------------------------------------------------------------------------------")
command = input("Zadejte pozadavek (otestuj/zobraz/konec): ")
print("---------------------------------------------------------------------------------------------------------------")

# funkce pro otestovani metod
def otestuj(vystupni_soubor):
    pass

# hlavni loop programu
while command != "konec":
    if command == "zobraz":
        view.zobraz()
    elif command == "otestuj":
        soubor = input("Zadejte nazev souboru pro zapsani dat: ")
        print("testuji...")
        otestuj(soubor)

    else:
        print("spatny pozadavek")

    command = input("Zadejte pozadavek (otestuj/zobraz/konec): ")


