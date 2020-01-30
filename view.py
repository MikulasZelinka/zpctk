import matplotlib.pyplot as plt
import math
import os
import sys
import random as rng


def zobraz():
    command = ""
    # osa = ["3.1", "3.14", "3.141", "3.1415", "3.14159", "3.141592", "3.1415926", "3.14159265"]
    osa = ["1", "2", "3", "4", "5", "6", "7", "8"]

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
	            with open (soubor) as f:
	                data = f.readlines()
	            data = [d.strip() for d in data]
	        except FileNotFoundError:
	            print("Tento soubor neexistuje")
	            return 
	
	        mc = [float(i) for i in data[0].split()]
	        metoda1 = [float(i) for i in data[1].split()]
	        metoda2 = [float(i) for i in data[2].split()]
	        metoda3 = [float(i) for i in data[3].split()]
	
	        plt.subplot(221)
	        plt.title("MonteCarlo", fontsize=11)
	        plt.plot(osa[:len(mc)], mc, "ro")
	        plt.xlabel("decimal places")
	        plt.ylabel("runtime (in seconds)")
	
	        plt.subplot(222)
	        plt.title("mc vizualizace", fontsize=11)
	        plt.plot(osa[:len(metoda1)], metoda1, "ro")
	        plt.xlabel("decimal places")
	        plt.ylabel("runtime (in seconds)")
	
	        plt.subplot(223)
	        plt.title("mc vizualizace", fontsize=11)
	        plt.plot(osa[:len(metoda1)], metoda1, "ro")
	        plt.xlabel("decimal places")
	        plt.ylabel("runtime (in seconds)")
	
	        plt.subplot(224)
	        plt.title("mc vizualizace", fontsize=11)
	        plt.plot(osa[:len(metoda1)], metoda1, "ro")
	        plt.xlabel("decimal places")
	        plt.ylabel("runtime (in seconds)")
	
	        plt.show()
	
	    elif command == "mc":
	        #number = int(input("Zadejte pocet bodu, ktere chcete nahodne vygenerovat: ")
	        pass
	
	    elif command == "exit":
                return	        
	
	    else:
	        print("Neplatny prikaz")
	
