''''
for si for each
'''
# exemplul cu dalmatienii
for i in range (0,102): # pentru ca ultimul va fi 101
    print(f'Dalmatianul cu nr {i}') # in intervalul acesta va numara, de la 0 la 101

# dac avrem sa schimbam pasul - din 2 in 2, adaugam 2 in range
# daca vrem sa se numere de la 1, schimbam range de la 1 la 102
for i in range(1, 102,2):  # pentru ca ultimul va fi 101
    print(f'Dalmatianul cu nr {i} numarat din 2 in 2')  # in intervalul acesta va numara, de la 0 la 101, indexul
    # inceep de la 0 si se numeroteaza (da valoarea) pana la 101, care de fapt este index 102

# parcurgerea unei liste cu ajutorul lui for prin intermediul indexului - dat de i
numere = [3, 70, 10, 20, 30]
for i in range (0, len(numere)):
    print(f'Indexul curent este {i}' ) # punem f inainte pentru a fi string.
    print(f'Numarul curent este {numere[i]}')


# for each
for numar in numere:
    print(f'Numarul curent este {numar}')
# suma numerelor
s=0