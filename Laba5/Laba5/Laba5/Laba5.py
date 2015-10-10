import random

print ('Ugadai chislo')
print ('''Vam nugno vvesti 2 chisla, odno bolche drugogo,
zatem ugadat chislo iz zadannogo diapazona,
kotoroe vubral computer''')

nachalnoeChislo = int (input('Vvedite nachalnoe chislo: '))
konechnoeChislo = int (input('Vvedite konechnoe chislo: '))
computerRandom = random.randint(nachalnoeChislo,konechnoeChislo)
otvet = int (input('Vach variant otveta: '))
schetchik = 1

while otvet != computerRandom:

    if  otvet > computerRandom:
        print ('Vache chislo > zagadannogo')
        otvet = int (input('Drugoi variant otveta: '))
        schetchik = schetchik + 1

    if  otvet < computerRandom:
        print ('Vache chislo < zagadannogo')
        otvet = int (input('Drugoi variant otveta: '))
        schetchik = schetchik + 1
                  
print ('Game over, Zagadanoe chislo: ', computerRandom)
print ('Ugadali s ', schetchik, ' raza')