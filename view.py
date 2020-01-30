import matplotlib.pyplot as plt
import math
import os
import sys
import random as rng


def zobraz():
    command = ""
    # vezme data ze souboru a graficky je zobrazi
    # zobrazi vizualizaci metody Monte Carlo
    while command != "exit":
        command = input("Zobrazit grafy nebo vizualizaci metody Monte Carlo? (grafy/mc/konec): ")
        if command == "grafy":

            slozka = os.listdir(os.curdir)
            print("Soubory: ")
            print("-------------------")
            for i in slozka:
                print(i, end="\n")
            print("-------------------")

            soubor = input('Zadejte nazev souboru: ')
            try:
                with open(soubor) as f:
                    data = f.readlines()
                    data = [d.strip() for d in data]
            except FileNotFoundError:
                print("Tento soubor neexistuje")
                return

            try:
                mc = [float(i) for i in data[0].split()]
                leibnitz = [float(i) for i in data[1].split()]
                sinus = [float(i) for i in data[2].split()]
                basel = [float(i) for i in data[3].split()]
            except IndexError:
                print("Spatny soubor")
                return

            # vykresleni 2x2 grafu, pro jednotlive metody

            plt.subplot(221)
            plt.title("MonteCarlo method", fontsize=11)
            plt.plot([i for i in range(len(mc))], mc, c="y", marker="v")
            plt.xlabel("decimal places")
            plt.ylabel("runtime (in seconds)")

            plt.subplot(222)
            plt.title("Leibnitz formula", fontsize=11)
            plt.plot([i for i in range(len(leibnitz))], leibnitz, c="r", marker="v")
            plt.xlabel("decimal places")
            plt.ylabel("runtime (in seconds)")

            plt.subplot(223)
            plt.title("Sinus formula", fontsize=11)
            plt.plot([i for i in range(len(sinus))], sinus, c="b", marker="v")
            plt.xlabel("decimal places")
            plt.ylabel("runtime (in seconds)")

            plt.subplot(224)
            plt.title("Basel formula", fontsize=11)
            plt.plot([i for i in range(len(basel))], basel, c="g", marker="v")
            plt.xlabel("decimal places")
            plt.ylabel("runtime (in seconds)")

            plt.show()

        elif command == "mc":
            # vizualizace metody Monte Carlo
            points = int(input("Zadejte pocet nahodne vybranych bodu (kvuli rychlosti doporucuji cislo v rozsahu 0 - 2500): "))
            i = 0
            total = 0
            inside = 0
            while i < points:
                x = rng.random()
                y = rng.random()
                if (x**2 + y**2) <= 1:
                    total += 1
                    inside += 1
                    plt.plot(x, y, "ro", alpha=0.25)
                else:
                    total += 1
                    plt.plot(x, y, "bo", alpha=0.25)
                i += 1

            plt.title("MonteCarlo")
            plt.show()

        elif command == "konec":
            return
        else:
            print("Neplatny prikaz")

