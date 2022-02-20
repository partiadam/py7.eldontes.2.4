'''
2.4 Feladat

A program egy listában tároljon öt darab szót, és abból véletlenszerűen válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit.
'''


from random import choice
szo = 'mindenható'
lista = [szo, 'alma', 'kutya', 'béka', 'tanulás']
kivalaszt = choice(lista)
eltalalta = []
nemtalaltael = []


while True:
    felhasznalo = input('Adj meg egy betűt: ')
    if felhasznalo in kivalaszt:
        print('Eltaláltad!')
        eltalalta.append(felhasznalo)
        print(eltalalta)
    else:
        print('Nem találtad el!')
        nemtalaltael.append(felhasznalo)
        print(nemtalaltael)
    if felhasznalo == '':
        break
    
    
print('A szó:', kivalaszt)