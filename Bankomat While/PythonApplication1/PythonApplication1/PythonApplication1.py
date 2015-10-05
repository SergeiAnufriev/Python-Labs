summ = str(input ('Vvedite summu: '))

ostatok = int(summ)

nominals = [500, 200, 100, 50, 20, 10, 5, 1]
nominalIndex = 0

while ostatok > 0 and nominalIndex < len (nominals):
    x = ostatok // nominals[nominalIndex]
    ostatok = ostatok - (x * nominals[nominalIndex])

    if x > 0:
       print (x, ' x ', nominals[nominalIndex], '$')
       
    nominalIndex = nominalIndex + 1
    


