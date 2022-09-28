# Cerinta: Fiind data o valoare de imprumut si un numar de luni in cate o variabila, sa se afiseze rata lunara luand in
# calcul dobanda 0% si comision 0%.

valoare_imprumut = int(input("Introduceti valoarea imprumutului (lei): "))
terment_credit = int(input("Durata creditului (luni): "))
print(f'Rata lunara: ', valoare_imprumut/terment_credit, "lei")