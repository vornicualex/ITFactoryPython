'''
Despre Py

Interpetor = interpreteaza fiecare linie. Ia codul de sus in jos
Cmpilarot = ia codul si transforma intre 1 si 0. Transforma codul
dynamically typed = poti pune orice tip de date. Spre deosebire de Java
ca aplicatii a devenit cel mai popular din lume -  intrecut Java
micropython suporta limbajul pytho, - micropy se poate isntala pe placute
In automatizari hw si sw
PEP8 - segulile de sintaxa Py
PEP20 - reguli de design, sa fie totul logic


PRINT
print -are nevoie de elemente de intrare

print() - va pune un spatiu

variabila = un spatiu in memorie numit menit sa fina o valoare - string int flow sau altceva
fiind memorata o putem folosi in viitor
print(1, 2, 3, 4, 5) - foloseste separatorul spatiu
daca nu e ok spatiu punem noi ce vrem sa folosimc a separator rint(1, 2, 3, 4, 5, sep='|')
se poate folosi si ultimul caracter, pus ca end= => print(1, 2, 3, 4, 5, sep='|', end='>')


comentarii. cu diez o singura line si se pune in dreptul liniei de cod
 comentariu cu 3 ghilimele ' ' ' se foloseste mai mult pentru explciatii
 mai exista print("Hello \n world!")  pe doua linii
control + click pe functie = ne duce automat in documentatia Py cu explciatii pentru fucntie



'''

print()

print(2)
print(15.3)
print('abc')

o_variabila = 'ceva text'
print(o_variabila)

print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, sep='|')
print(1, 2, 3, 4, 5, sep='|', end='>')

print()
print()
print()


print('cum se face print')
print('Hello world!')
print("Hello\nworld!")
print('sau')#sau
print('''Hello
world!''')

print()
print()
print()

# variabile si tipuri de date
#are nume unic
# a=1
# cu a=2 inlocuim valaorea variabilei a
# fara spatii = snake_case. Adica folosim underscore
#j =radical pe -1, pentru ca nu punem valori cu minus
# atentie la denumirea variabilei sa nu fie acelasi nume ca variabila in sine

#fucntia type
print(type(2))
print(type(12.5))
print(type(True))
print(type("abc"))
un_tip = type(None)
print(un_tip)
#print('clasa variabilei un_tip este'print(un_tip))

#fucntia type
un_int = int("20")
un_alt_int = int(273.15)
un_float = float("3.14")
print()

print(un_int, un_alt_int, un_float)
#sau pe raduri separate
print(un_int, un_alt_int, un_float, sep='\n')
print()
print('daca vrem spatii intre randusi si ceva la sfarsit')
print(un_int, un_alt_int, un_float, sep='\n\n', end='>>>') # daca vrem ceva la final

print()
print()
print('OPERATORI')
#OPERATORI
#ne intereseaza mult catul si restul impartirii
rezultat_impartire = 5 / 2
cat_impartire = 5 // 2
rest_impartire = 5 % 2
putere = 5 ** 2
print(rest_impartire, cat_impartire, rezultat_impartire, putere, sep='\n')
print('radical din 3')
print(3**(1/2))
print('radical de ordin 3')
print(21**(1/3))

print()
#operatori de atribuire
print('operatori de atribuire')
a = 10
a += 2  # a = a + 2
a -= 3  # a = a - 3
a *= 2  # ...
a /= 3
a //= 2
a %= 3
a **= 2
print(a) #sfarsitul rezultatului este 0

print()
#operatori de comparatie => returneaza true sau false
print(2 > 5)  # mai mare
print(2 < 5)  # mai mic
print(2 == 5)  # egal
print(2 <= 5)  # mai mic sau egal
print(2 >= 5)  # mai mare sau egal
print(2 != 5)  # diferit

print()
print()

#operatori logici

''''
si = True and False  # operatia "si" - toate trebuie sa se confirme
sau = True or False  # operatia "sau" - doar una tre sa fie true
negare = not True  # operatia de negare
'''
'''tinem cont de ordinea operatiilor
radicali, ridicari la putere, apoi inmultire, impartire, adunare, scadere. folosim doar 
paranteze rotunde pentru operatii
'''

#operatori speciali
print('operatori speciali')
texte_concatenate = "ceva" + " inca ceva"  + '    -se aduna info pe acelasi rand'
text_repetat = "-" * 20
print(texte_concatenate, text_repetat, sep='\n')

#functia input - are nevoie de o valoare de la tastatura

