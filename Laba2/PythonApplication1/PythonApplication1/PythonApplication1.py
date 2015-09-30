f = input ("Vvedite vachu familily: ")
i = input ('Vvedite vache imya: ')
o = input ('Vvedite vache otchestvo: ')
d = str (input ('Vvedite datu rogdenya: '))
a = str (input ('Vvedite adres: '))



print ('\n' + 'vacha familia: ' + f + '\n')
print ('vache imya: ' + i + '\n')
print ('vache otchestvo: ' + o + '\n')
print ('vacha data rogdenya: ' + d + '\n')
print ('vach adres: ' + a + '\n')
print ('Super, teper u nas ect na was KOMPROMAT' + '\n')

t = open ('text.txt', 'w')
t.write ('vacha familiya: ' + f + '\n')
t.write ('vache imya: ' + i + '\n')
t.write ('vache otchestvo: ' + o + '\n')
t.write ('vacha data rogdenya: ' + d + '\n')
t.write ('vach adres: ' + a + '\n')
t.write ('Super, teper u nas ect na was KOMPROMAT' + '\n')
t.close ()