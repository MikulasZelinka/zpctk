import matplotlib.pyplot as plt
import math
import os
import random as rng


# nacte slovnik ze souboru
def nacti(soubor):
    f = open(soubor)
    data = f.read()
    f.close()
    return eval(data)

# dynamicke vykresleni grafu (lepsi vyskladani subplotu)
def vykresli(data):
    plt.figure(figsize=(20, 10))
    plt.tight_layout()

    x = math.floor(math.sqrt(len(data)))
    y = math.ceil(math.sqrt(len(data)))
    p = 1

    for i in data:
        plt.subplot(x, y, p)
        plt.title(i, fontsize=11)
        plt.plot([i for i in range(len(data[i]))], data[i], c="r", marker="v")
        plt.xlabel("decimal places")
        plt.ylabel("runtime (in seconds)")
        p += 1

    plt.subplot(x, y, p)
    plt.title("Comparison of all methods")

    for i in data:
        plt.plot(data[i], marker="v", label=i, alpha=0.6)

    plt.xlabel("decimal places")
    plt.ylabel("runtime (in seconds)")

    plt.legend()
    plt.xlim(0, 20)
    plt.xticks(range(21))
    plt.grid(alpha=0.2)
    fig = plt.gcf()
    plt.show()
    fig.savefig('./pictures/results.png')



# vezme data ze souboru a graficky je zobrazi
# zobrazi vizualizaci metody Monte Carlo
def zobraz():
    command = ""
    while command != "exit":
        command = input("Zobrazit grafy nebo vizualizaci metody Monte Carlo? (grafy/mc/konec): ")
        if command == "grafy":

            # vylistovani slozky se skriptem
            slozka = os.listdir(os.curdir)
            print("Soubory: ")
            print("-------------------")
            for i in slozka:
                print(i, end="\n")
            print("-------------------")

            # vybrani souboru
            soubor = input('Zadejte nazev souboru: ')

            # existuje soubor? + nacteni souboru
            try:
                data = nacti(soubor)
            except:
                print("Tento soubor neexistuje/neni validni")
                return


            # vykresleni grafu
            vykresli(data)

        # vykresleni metody Monte Carlo
        elif command == "mc":
            points = int(input("Zadejte pocet nahodne vybranych bodu (kvuli rychlosti doporucuji cislo v rozsahu 0 - 2500): "))
            i = 0
            total = 0
            inside = 0
            while i < points:
                x = rng.random()
                y = rng.random()
                # pokud je bod vevnitr, vykresli cervene
                if (x**2 + y**2) <= 1:
                    total += 1
                    inside += 1
                    plt.plot(x, y, "ro", alpha=0.25)
                # pokud je bod venku, vykresli modre
                else:
                    total += 1
                    plt.plot(x, y, "bo", alpha=0.25)
                i += 1
            plt.axis([0, 1, 0, 1])
            plt.title("MonteCarlo")
            plt.show()

        # ukonceni view.py
        elif command == "konec":
            return
        else:
            print("Neplatny prikaz")

