import random as rng
import math
import time
import decimal

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
        for _ in range(10**5):
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

def piChudnovsky(timeout, precision):
    # popis: https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    # source: https://dev.to/parambirs/til-calculating-n-digits-of-pi-using-chudnovsky-algorithm-1j10
    start = time.time()
    global ref

    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409
    S = L
    i = 1

    while True:
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X

        pi = C / S

        end = time.time()
        if (end - start >= timeout) or (round(pi, precision) == round(decimal.Decimal(ref), precision)):
            return end - start

        i += 1
