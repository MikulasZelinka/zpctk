import random as rng
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
    while total <= n*10*4:
        a = rng.random()
        b = rng.random()
        if (a*a + b*b) <= 1:
            inside += 1
            total += 1
        else:
            total += 1
    pi = 4*(inside/total)
    end = time.time()
    #runtime = round(end - start, 3)
    runtime = end - start
    return pi, runtime

def Gregory(n):
    start = time.time()
    denominator = 1
    term = 'even'
    pi = 0
    for i in range(n):
        if term == 'even':
            pi = pi + (1/denominator)
            denominator += 2
            term = 'odd' 
        else:
            pi = pi - (1/denominator)
            denominator += 2
            term = 'even'
    end = time.time()
    #runtime = round(end - start, 3)
    runtime = end - start
    pi = 4*pi
    return pi, runtime


def Archimedes(n):
    pass

def Machin(n):
    pass

def Gauss(n):
    pass

def Sinus(n):
    start = time.time()
    pi = 3
    for i in range(n):
        pi = pi + math.sin(pi)
    end = time.time()
    #runtime = round(end - start, 3)
    runtime = end - start
    return pi, runtime

#for i in range(10):
#    print(Sinus(i))

#print(MonteCarlo(10))
iterace = int(input())
print('Gregory: ', Gregory(iterace))
print('Sinus: ', Sinus(iterace))
print('MC: ', MonteCarlo(iterace))
