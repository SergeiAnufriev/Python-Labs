x = 0;


while x != 'q':
    try:
        x = input('enter the number:')
        intx = int(x)
        y = intx ** 2
        print (y)

        z = (str(x) + ' * ' + str(x) + ' = ' + str(y))
        
        def add (): 
            f = open ('text.txt', 'a')  
            f.write(z + '\r\n') 
            f.close ()
            return add ()

    except Exception:
        if x != 'q':
            print('Wrong input data')


    

#print('that would finalize press "1"')
#print('that would continue the work, press "2"')     
#exit = input ('enter the number "1" or "2":')
#if exit == 1 
    