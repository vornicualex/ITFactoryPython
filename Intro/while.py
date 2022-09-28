'''
while = un loop, un ciclu repetitiv care verifica o contitie
zona de cod care se repeta atat timp cat o conditie este ture
'''

#problema: masina merge cat timp are benzina

litri_benzina = 10
while litri_benzina > 0:
    # acceleram
    print('Acceleram')
    #scad litri benzina
    litri_benzina = litri_benzina - 1
    if litri_benzina <= 3:
        print('Martor bord rosu')

print('Stop')