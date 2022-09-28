'''
Recap:
variabile
tipuri de date: string = siruri de caractere introduse cu ghlimele duble, int = numar intreg, char= un singur caracter,
boolean = true/false, float (Py)/double (Java) = numere zecimale,

NEW!!!

Operatori:
Artitmetici: +, -, *, /, % (modulo = aflarea restului impartirii)
De comparare: <>, ==, != (diferit), >=, <=
Logici: and (and), or (or), ! (not)

Flow control = conditionale - if else
'''

#Exemple
a = 3
b = 5

# test operatori artmetici
print(a - b) #3-5 =>-2
print(a + b) #3+5 => 8

# test operatori comparare
print(a == b) # 3 = 5? => False
print(a < b) # 3 < 5? => True

# test operatori logici
print(a < b and a < 4) # true si true => True
print(a < b or a < 2) # true sau false => True (SAU inseamna ca e de ajuns sa fie doar unul adevarat)

# Exercitiu!
# La scoala la sedinta cu parintii poti sa vii: cu mama sau cu tata sau ((cu bunicul si bunica)
mama = True
tata = False
bunicul = False
bunica = False
print (mama or tata or (bunicul and bunica))

# Tesatare flow control control = conditionale - if else - pe fisier separat
# evalueaza conditii si bifurca codul in fucntie de rezultat



