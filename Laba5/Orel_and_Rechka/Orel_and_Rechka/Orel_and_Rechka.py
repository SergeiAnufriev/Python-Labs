import random

kolichestvoBroskov = int (input('Vvedite colicestvo broskov: '))
brosok = 1
orel = 0
rechka = 0


while brosok < kolichestvoBroskov + 1:
    rezultat = random.randint(1, 2)

    if rezultat > 1:
        rechka = rechka + 1

    else:
        orel = orel + 1 

    brosok = brosok + 1
print ('Orel = ', orel)
print ('Rechka = ', rechka)
