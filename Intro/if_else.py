# Tesatare flow control control = conditionale - if else
# evalueaza conditii si bifurca codul in fucntie de rezultat

piesa_faina = True
print('pornim radio')
if piesa_faina == True:
    print('dam mai tare radio')
    print('fredonam piesa')
print('oprim radio')

# schimbam variabila piesa_faina cu true / false si avem rezultate diferite!!!

# if else
# daca numarul este par printam acest lucru
# altfel printam impar
nr = 4
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? ne da restul 0 => folosim modulo (%)
if (nr % 2) == 0:
    print('numar par')
else:
    print('impar')

# Schimbam numarul si avem raspuns diferit!!!

# este un numar pozitiv?
if nr >0:
    print('pozitiv')
else:
    print("nr nu este pozitiv")

    # tema!!! daca utilizatorul are < 18 ani, nu poate paria, alfel poate.

# if, else if, else
# robot care ne saluta cand se deschide usa, in fucntie de ora
        # luam date de la tastatura
            # pentru ca ora este un numar, transformam imputul din string (cum s-ar citi automat in Py) in int
# ora = int(input('Introdu ora  '))
# if (ora < 0):
#     print('ora negativa/ introdu o ora intre 0-24')
# elif ora <= 11:
#     print('Buna dimineata!')
# elif ora <= 18:
#     print('Buna ziua!')
# elif ora <= 21:
#     print('Buna seara!')
# elif ora <= 24:
#     print('Noapte buna!')
# else:
#     print('Eroare - ora invalida')

# EXERCITIU: Contorizam viteza unei masini: < 0 viteza invaliza, 0 inseamna ca stationeaza, < 50 in localitate, <80 pe DJ, >90 pe autostrada
        #!!! Cand vrei sa comentam (excludem din program linii) mai multe linii active, selectam liniile si Ctrl+/. Decomentarea se face la fel.

# Alternativa la switch specifica Java
# robot telefonic
optiune = int(input('Alege optiune '))
if optiune == 0:
    print('Meniu anterior')
elif optiune == 1:
    print('Ati ales limba RO')
elif optiune == 2:
    print ('Ati ales limba EN')
else:
    print('Nu am identificat optiuea din lista. Alege tasta corecta')
