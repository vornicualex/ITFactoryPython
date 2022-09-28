# in Py nu avem map. Se numeste dict
lista_goala = []
dict_gol = {}




# declaram si initializam un dict (dictionary)
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 7}
print(note_elevi)
#adaugare elemente
note_elevi ['Sebi'] = 5

#printam noul dict
print(note_elevi)

#aflam elemente din interior
print('Nota lui Sebi este:', note_elevi['Sebi'])
print('Nota lui Ana este:', note_elevi.get('Ana'))

# actualizam valori:
note_elevi['Costel'] = 10
print(note_elevi)

#aflam dimensiune:
print(len(note_elevi))

#stergem valor:
note_elevi.pop('Gigel') # .pop sterge si returneaza valoarea
print(note_elevi)

print(note_elevi, "Gigel", note_elevi.get('Gigel', 'nu mai este in sistem')) #daca dam get acum nu mai exista Gigel insa ii putem pune un mesaj

#returneaza doar cheile
print(note_elevi.keys())

