import random

kolichestvoBroskov = int (input('Vvedite colicestvo broskov: '))
orel = 0
rechka = 0


for _ in range(kolichestvoBroskov):
    rezultat = random.randint(1, 2)

    if rezultat > 1:
        rechka = rechka + 1

    else:
        orel = orel + 1 

print ('Orel = ', orel)
print ('Rechka = ', rechka)
