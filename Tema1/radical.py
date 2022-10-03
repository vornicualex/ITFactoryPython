# Cerinta:
# Fiind dat un numar citit de la tastatura, sa se afiseze radicalul lui.

# numar_citit = int(input("Introduceti o valoare: "))
# #print(type(numar_citit))
# print('Radical din valoarea indrousa este:')
# print(numar_citit**(1/2))

numar_citit = input("Introduceti o valoare: ")
numar = int(numar_citit)

radical = numar**(1/2)
#print(numar**(1/2))
print(radical)
print(f'Radical din', numar_citit, "este:", radical)
print('Verificare rezultat:',radical**2==numar)