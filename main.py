from collections import defaultdict

import methods      # methods.py    <---> testovane metody
import view         # view.py       <---> zobrazeni
import math

'''
   toto je hlavni cast programu
   zavolani testovani vsech metod, zapsani jejich vysledku do souboru a posleze vypsani
   program se bude ovladat z konzole
   vse bude bezet, dokud uzivatel nezada 'konec'
'''

MAX_PREC = 1000
ref = math.pi # referencni hodnota pi
command = ""
data = defaultdict(list) # zde jsou docasne ulozena data pred zapsanim do souboru
metody = [i for i in dir(methods) if i.startswith("pi")] # zde se dynamicky ukladaji nazvy metod z modulu view.py pro otestovani
# pro pridani dalsi metody ji staci dopsat se spravnou predponou("pi") do methods.py

print("Tento program porovnava iterativni metody approximace pi na zaklade casu behu programu")
print("---------------------------------------------------------------------------------------------------------------")
print("Porovnavame nasledujici metody: MonteCarlo, Leibnitzova formule, Sinus formule, Basel formule, Chudnovsky")
print("---------------------------------------------------------------------------------------------------------------")
command = input("Zadejte pozadavek (otestuj/zobraz/konec): ")
print("---------------------------------------------------------------------------------------------------------------")


# funkce pro zapsani slovniku do souboru
def uloz(slovnik, soubor):
    f = open(soubor, "w")
    f.write(str(dict(slovnik)))
    f.close()


# hlavni loop programu
while command != "konec":
    if command == "zobraz":
        view.zobraz()
    elif command == "otestuj":
        precision = int(input(f"Zadejte maximalni pocet desetinnych mist do ktereho testovat (1 - {MAX_PREC}): "))
        if precision < 1 or precision > MAX_PREC:
            print("Mimo rozsah")
        else:
            timeout = int(input("Zadejte timeout pro kazdy test (v s): "))
            soubor = input("Zadejte nazev souboru pro zapsani dat: ")
            
            # otestovani kazde metody se zadanymi parametry
            for m in metody:
                for p in range(precision):
                    print("Testing", m, "to", p+1, "decimal places")
                    value = getattr(methods, m)(timeout, p+1)
                    data[m].append(value)
                    if value > timeout:
                        break

            print(data)
            uloz(data, soubor)
    else:
        print("spatny pozadavek")

    command = input("Zadejte pozadavek (otestuj/zobraz/konec): ")

# ukonceni programu
print("program ukoncen")
