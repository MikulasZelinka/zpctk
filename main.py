import methods      # methods.py    <---> testovane metody
import view         # view.py       <---> zobrazeni
import time
import os
import math

'''
   toto je hlavni cast programu
   zavolani testovani vsech metod, zapsani jejich vysledku do souboru a posleze vypsani
   program se bude ovladat z konzole
   vse bude bezet, dokud uzivatel nezada 'konec'
'''

ref = math.pi # referencni hodnota pi
command = ""
data = [[], [], [], []]

print("Tento program porovnava iterativni metody approximace pi na zaklade casu behu programu")
print("---------------------------------------------------------------------------------------------------------------")
print("Porovnavame nasledujici metody: MonteCarlo, Leibnitzova formule, Sinus formule, ")
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

        precision = int(input("Zadejte maximalni pocet desetinnych mist do ktereho testovat: "))
        timeout = int(input("Zadejte timeout pro kazdy test (v s): "))
        soubor = input("Zadejte nazev souboru pro zapsani dat: ")

        for i in range(precision):
            value = methods.MonteCarlo(timeout, i+1)
            print("Testing MonteCarlo to ", i+1, " decimal places") 
            if value < timeout:
                data[0].append(value)
            else:
                break

        for i in range(precision):
            value = methods.Leibnitz(timeout, i+1)
            print("Testing Leibnitz to ", i+1, " decimal places") 
            if value < timeout:
                data[1].append(value)
            else:
                break

        for i in range(precision):
            value = methods.Sinus(timeout, i+1)
            print("Testing Sinus to ", i+1, " decimal places") 
            if value < timeout:
                data[2].append(value)
            else:
                break

        vystup = open(soubor, "w+")

        for i in data:
            vystup.write(" ".join(map(str, i)))
            vystup.write("\n")

        vystup.close()

    else:
        print("spatny pozadavek")

    command = input("Zadejte pozadavek (otestuj/zobraz/konec): ")

print("goodbye!")
