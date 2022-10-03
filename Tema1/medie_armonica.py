# Cerinta: Fiind date 3 numere citite de la tastatura, sa se afiseze media lor armonica.
print('Calcul media armonica:')
a = int(input("a="))
b = int(input("b="))
c = int(input('c='))
mar = (3*a*b*c)/(a*b+a*c+b*c)
mar2 = 3/((1/a)+(1/b)+(1/c))

print("Media armonica este:",mar)
print("Media armonica este:",mar2)