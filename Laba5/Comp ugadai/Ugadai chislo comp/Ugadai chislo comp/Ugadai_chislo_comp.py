import random

print ('Ugadai chislo')
print ('''Vam nugno vvesti 2 chisla, odno bolche drugogo,
zatem computer ugadaet chislo iz zadannogo diapazona,
s vachimi podskazkami''')

nachalnoeChislo = int (input('Vvedite nachalnoe chislo: '))
konechnoeChislo = int (input('Vvedite konechnoe chislo: '))
otvet = int (input ('Zagadaite chuslo iz zadannogo diapazona: '))
computerRandom = random.randint(nachalnoeChislo, konechnoeChislo)


while computerRandom != otvet:
    print ('otvet', computerRandom, '?')
    print ('Esli danoe chislo < zagadannogo, nagmite 1')
    print ('Esli danoe chislo > zagadannogo, nagmite 2')
    podskazka = int (input('Vvedite 1 ili 2: '))

    if podskazka == 1:
        computerRandom = random.randint(computerRandom + 1, konechnoeChislo)
    
    if podskazka == 2:
        computerRandom = random.randint(nachalnoeChislo, computerRandom - 1)

print ('Vache chislo ugadali, otvet = ', computerRandom)
     
        
         