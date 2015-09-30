summ = input ('Vvedite summu: ')

if summ < 0:
    print ('Game over')
else:             
    a = ( summ / 500)
    b = summ - (500 * a)
    print (a, ' x 500$')

    c = ( b / 200)
    d = b - (200 * c)
    print (c, ' x 200$')

    e = ( d / 100)
    f = d - (100 * e)
    print (e, ' x 100$')

    g = ( f / 50)
    k = f - (50 * g)
    print (g, ' x 50$')

    w = ( k / 20)
    q = k - (20 * w)
    print (w, ' x 20$')

    r = ( q / 10)
    t = q - (10 * r)
    print (r, ' x 10$')

    y = ( t / 5)
    u = t - (5 * y)
    print (y, ' x 5$')
  
    i = ( u / 1)
    o = u - (1 * i)
    print (i, ' x 1$')

