import random as rng
import matplotlib.pyplot as plt
import math
import time

''' 
    zde budou vsechny funkce, ktere budeme testovat
    kazda funkce vraci cas behu
    na vstupu funkce je timeout 
    nazvy funkci maji predponu pi, kvuli dynamickemu nacteni v main
'''
ref = math.pi

def piMonteCarlo(timeout, precision):
    # metoda Monte Carlo
    start = time.time()
    global ref
    inside = 0
    total = 0
    end = 0
    pi = 0
    # podminka pro zadany runtime
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

def piLeibnitz(timeout, precision):
    # vyuzivame tento vztah 4 - 4/3 + 4/5 - 4/7 + 4/9 ... = pi
    start = time.time()
    global ref
    denominator = 1
    term = 2
    pi = 0
    end = 0
    while end - start < timeout and round(pi, precision) != round(ref, precision):
        if term == 2: 
            pi = pi + (4/denominator)
            denominator += 2
            term = 1
        else:
            pi = pi - (4/denominator)
            denominator += 2
            term = 2
        end = time.time()
    runtime = end - start
    return runtime


def piSinus(timeout, precision):
    # vyuzivame faktu, ze tato funkce konverguje k pi
    start = time.time()
    global ref
    pi = 3
    end = 0
    while end - start < timeout and round(pi, precision) != round(ref, precision):
        pi = pi + math.sin(pi)
        end = time.time()

    runtime = end - start
    return runtime

def piBasel(timeout, precision):
    # 1/1^2 + 1/2^2 + 1/3^2 + ... = (pi^2)/6
    start = time.time()
    global ref
    end = 0
    pi = 0
    denominator = 1
    while end - start < timeout and round(math.sqrt(pi*6), precision) != round(ref, precision):
        pi = pi + 1/(denominator**2)
        denominator += 1
        end = time.time()

    runtime = end - start
    return runtime

