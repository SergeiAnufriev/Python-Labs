import datetime

gr = input ('god r: ')
#g = input ('god: ')
#m = input ('mesyaz: ')
#d = input ('den: ')

#g1 = g - gr
#x = 12 - mr 
#y = 30 - dr 

#z = (g1 * 365) + ((x + m) * 30) + dr + d
#rez = str ( z * 86400)
#print ('vsch vozrast: ' + rez + ' cekynd')

if gr > 2016:
    print ('Game over')
else:     
    mr = input ('mesyaz r: ')
    dr = input ('den r: ')
    dBirth = datetime.datetime(gr, mr, dr)
    rez = datetime.datetime.today() - dBirth

    print (rez.total_seconds())