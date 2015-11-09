import math

print ('Programma dlya recheniya kvadratnogo uravneniya')
a = float (input('Vvedite kofizient, a: '))
b = float (input('Vvedite kofizient, b: '))
c = float (input('Vvedite kofizient, c: '))

if a != 0:
	D = b ** 2 - 4 * a * c

	if D > 0:
		x1 = (- b + math.sqrt(D)) / (2 * a)
		x2 = (- b - math.sqrt(D)) / (2 * a)
		print ('x1 = ', x1)
		print ('x2 = ', x2)
	elif D == 0:
		x = (- b * 2) / (2 * a)
		print ('x =', x)
	else:   
		print ('There is not real roots of  equation ')
else:
	print ('Input error: coefficient a must be nonzero')




