import random as rng
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import math
import time

''' 
    zde budou vsechny funkce, ktere budeme testovat
    kazda funkce vraci aproximaci pi, cas behu
    na vstupu funkce je pocet iteraci (pro MonteCarlo je iteraci vybrani 10**6 nahodnych bodu)

'''

def MonteCarlo(n):
    start = time.time()
    inside = 0
    total = 0
    while total <= n*1000000:
        a = rng.random()
        b = rng.random()
        if (a*a + b*b) <= 1:
            inside += 1
            total += 1
        else:
            total += 1
    pi = 4*(inside/total)
    end = time.time()
    runtime = end - start
    return pi, runtime

def GLeib(n):
    pass

def Arch(n):
    pass

def Machin(n):
    pass

def Gauss(n):
    pass

def Sinus(n):
    pi = 3
    for i in range(n):
        pi = pi + math.sin(pi)
    return pi

#for i in range(10):
#    print(Sinus(i))

#print(MonteCarlo(10))
