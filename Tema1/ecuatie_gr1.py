# Cerinte: Fiind date 2 numere a, b, sa se afiseze solutia x ecuatiei de gradul 1: a * x + b = 0
print('Calcul x din ecuatia de gradul 1  (a * x + b = 0):')
a = int(input("a="))
b = int(input("b="))
x = -b/a
print("Valoarea lui x este:",x)
print('Verificare a*x+b=0:',a*x+b==0)
