   
exit = 1
while exit == 1:  
  
    summ = float(input ('Vvedite summu: '))

    ostatok = summ

    nominals = [500, 200, 100, 50, 20, 10, 5, 1]
    nominalIndex = 0

    while ostatok > 0 and nominalIndex < len (nominals):
        x = ostatok // nominals[nominalIndex]
        ostatok = ostatok - (x * nominals[nominalIndex])

        if x > 0:
           print (x, ' x ', nominals[nominalIndex], '$')
       
        nominalIndex = nominalIndex + 1

    print ('Hotite povtorit? vvedite 1')
    print ('Hotite zaverchit rabatu? vvedite 2')

    exit = int (input( 'Vvedite 1 and 2: '))


    


