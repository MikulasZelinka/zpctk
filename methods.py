import random as rng
import matplotlib.pyplot as plt
import numpy as np
import math
import time

''' 
    zde budou vsechny funkce, ktere budeme testovat
    kazda funkce vraci cas behu a aproximaci pi
    na vstupu funkce je start a timeout 
'''
ref = math.pi

def MonteCarlo(start, timeout, precision):
    global ref
    inside = 0
    total = 0
    end = 0
    pi = 0
    while end - start < timeout and round(pi, precision) != round(ref, precision):
        end = time.time()
        for i in range(10**5):
            a = rng.random()
            b = rng.random()
            if (a*a + b*b) <= 1:
                inside += 1
                total += 1
            else:
                total += 1
        pi = 4*(inside/total)
    runtime = end - start
    return runtime

def Gregory(start, timeout, precision):
    global ref
    denominator = 1
    term = 'even'
    pi = 0
    end = 0
    while end - start < timeout and round(4*pi, precision) != round(ref, precision):
        if term == 'even':
            pi = pi + (1/denominator)
            denominator += 2
            term = 'odd' 
        else:
            pi = pi - (1/denominator)
            denominator += 2
            term = 'even'
        end = time.time()

    runtime = end - start
    pi = 4*pi
    return runtime


def Archimedes(n):
    pass

def Machin(n):
    pass

def Gauss(n):
    pass

def Sinus(start, timeout, precision):

    global ref
    pi = 3
    end = 0

    while end - start < timeout and round(pi, precision) != round(ref, precision):
        pi = pi + math.sin(pi)
        end = time.time()

    runtime = end - start
    return runtime

print(round(ref, 3))
print('Gregory: ', Gregory(time.time(), 5, 3))
print('Sinus :', Sinus(time.time(), 5, 3))
print('MonteCarlo: ', MonteCarlo(time.time(), 5, 3))
