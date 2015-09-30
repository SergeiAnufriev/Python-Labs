summ = int(input ('Vvedite summu: '))

if summ < 0:
    print ('Game over')
else:             
    a = ( summ // 500)
    b = summ - (500 * a)
    
    c = ( b // 200)
    d = b - (200 * c)
 
    e = ( d // 100)
    f = d - (100 * e)
   
    g = ( f // 50)
    k = f - (50 * g)  

    w = ( k // 20)
    q = k - (20 * w)
   
    r = ( q // 10)
    t = q - (10 * r)
  
    y = ( t // 5)
    u = t - (5 * y)
   
    i = ( u // 1)
    o = u - (1 * i)

if a > 0:
    print (' ', a, 'x 500$')
    
if c > 0:
   print (' ', c, 'x 200$')

if e > 0:
   print (' ', e, 'x 100$')

if g > 0:
   print (' ', g, 'x 50$')

if w > 0:
    print (' ', w, 'x 20$')

if r > 0:
   print (' ', r, 'x 10$')

if y > 0:
   print (' ', y, 'x 5$')

if i > 0:
   print (' ', i, 'x 1$')


