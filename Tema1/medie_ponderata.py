# Cerinta: Fiind date 3 numere a, b, c si 3 ponderi p, q, r sa se afiseze media lor ponderata. Valorile variabilelor pot fi
# hardcoded.

print('Calcul media ponderata:')
a = int(input("numar a="))
b = int(input("numar b="))
c = int(input("numar c="))
p = int(input("pondere p="))
q = int(input("pondere q="))
r = int(input("pondere r="))
mpond = ((p*a)+(q*b)+(r*c))/(p+q+r)
print("Media ponderata este:", mpond)