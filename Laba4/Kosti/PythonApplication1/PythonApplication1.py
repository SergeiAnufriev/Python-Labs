import random

#exit = 1

print ('Igra v kosti')

while True:

    kubik1 = random.randint(1, 6)
    kubik2 = random.randint(1, 6)
    rezultat = kubik1 + kubik2
    print ('kubik 1 = ', kubik1)
    print ('kubik 2 = ', kubik2)
    print ('summa = ', rezultat)

    print ('Hotite povtorit? vvedite 1')
    print ('Hotite zaverchit rabatu? vvedite 2')

    if (input( 'Vvedite 1 and 2: ')).lower() == "2" : break