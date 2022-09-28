#Py lucreaza cu Liste. e mai smart. Array in Py tot cu liste se executa.
# listele in Py pot sa cumprinda elemente de tipuri diferite
#au dimensiune dinamica

fructe = ['mar', 'banana', 3, 'portocala', 3, True, 3, 'cirese', 'mandarina', 'cirese', 'cirese']

#Afisare lista:
print(fructe)

# accesare element in fucntie de index
print(fructe[0])
print(fructe[1])

# adaugam un nou emelent in lista
fructe.append('rosie')

print(fructe)

# suprascriem un element
# in loc de mar punem para
fructe[0]= 'para'
print('Lista de fructe: ', fructe)

# dimensiune lista
print('Dimensiune lista - cate linii are lista: ', len(fructe))

# scoate si ne returneaza (da) ultimul element
last = fructe.pop()
print('ultimul element: ', last) #ne da ultimul element chiar daca e scos
print('noua lista: ', fructe) # noua lista

#de cate oriu apare un element
print('Cate cirese sunt in lista de fructe: ', fructe.count('cirese')) #punem elementul din lsita fructe pe care vrea sa il numere. elementele de tip string se pun cu ghilimele simple

#lista noua de fructe
fructe_exotice = ['ananas','kiwi']
#extintem lista de fructe initiala cu lista de exotice
fructe.extend(fructe_exotice)
print('Lista de fructe initiala extinsa cu lista de fructe exotice: ', fructe)