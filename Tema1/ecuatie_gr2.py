# Cerinte: Fiind date 3 numere a, b, c, sa se afiseze solutiile x1, x2 ale ecuatiei de gradul 2: a * x ** 2 + b * x + c = 0.

print('Calcul x1, x2 din ecuatia de gradul 2:')
a = int(input("numar a="))
b = int(input("numar b="))
c = int(input("numar c="))
delta = b**2-4*a*c
x1=(-b+delta**(1/2))/(2*a)
x2=(-b-delta**(1/2))/(2*a)
x12=-b/(2*a)
ii=1
x11=(-b+ii*(-delta)**(1/2))/(2*a)
x22=(-b-ii*(-delta)**(1/2))/(2*a)
if delta > 0:
    print(f'Delta >0, X1 este: ', x1,', X2 este: ', x2)
else:
    if delta < 0:
        print(f'Delta <0, X1=X2 este: ', x12)
    else:
        if delta == 0:
            print(f'Delta =0, X1 este:', x11, 'X2 este:', x22)
        else:
            print ("Cedva nu este corect")