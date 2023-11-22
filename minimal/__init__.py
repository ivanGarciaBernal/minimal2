from sympy import sqrt

def es_potencia(k,n):
    return int(k**(1/n)) ** n == k

def potencia_fibonacci(n, pot=2):
    fibs = []
    a, b = 0, 1
    while a < n:
        if es_potencia(a,pot):
            fibs.append(a)
        a, b = b, a+b
    return fibs
