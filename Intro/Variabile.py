# variabila = zona din memoria unui PC care tine date
# variabila = o cutie in care punem valori

# EX: ne gandim la o masina ce are marca si model
# am declarat si initializat variabila marca
marca_masina = 'Volvo'
model_masina = 'XC 60'

# numele variabilelor se da doar cu litera mica si fara spatii


# loosely typed = nu trebuie sa specificam tipurile de date al variabilelor cu care lucram
# py e mai relaxat. putem defini variabilele cum dorim, fara strictete (cum e la Java cu String, Number and so on)

# folosim variabilele declarate
print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul {model_masina}')

# suprascriere overwrite - in cazul in care se schimba info din variabile
model_masina= 'XC60 Facelift'

print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul {model_masina}')

nume= 'Alex'
prenume= 'Vornicu'
varsta= 35
print(prenume +' ', nume)
# print(prenume +' ', +nume, +varsta) nu va merge pentru ca nu poate interpreta +varsta
print(f'Proprietar {nume, prenume}')
print(f'Proprietar {nume} {prenume}')
print(f'Proprietar {nume} {prenume} {varsta}')
print(f'Varsta {varsta}')