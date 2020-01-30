import random as rng
import matplotlib.pyplot as plt
import math
import time

''' 
    zde budou vsechny funkce, ktere budeme testovat
    kazda funkce vraci cas behu a aproximaci pi
    na vstupu funkce je start a timeout 
'''
ref = math.pi

def MonteCarlo(start, timeout, precision):
    # 
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

def Leibnitz(start, timeout, precision):
    # vyuzivame tento vztah 4 - 4/3 + 4/5 - 4/7 + 4/9 ... = pi
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
    print(pi)
    runtime = end - start
    return runtime


def Archimedes(start, timeout, precision):
    global ref

    pass

def Machin(start, timeout, precision):
    global ref
    pass

def Gauss(start, timeout, precision):

    global ref
    pass

def Sinus(start, timeout, precision):
    # vyuzivame faktu, ze tato funkce konverguje k pi
    global ref
    pi = 3
    end = 0
    while end - start < timeout and round(pi, precision) != round(ref, precision):
        pi = pi + math.sin(pi)
        end = time.time()

    runtime = end - start
    return runtime

