print('''Program print chast number, znachenie poslednego 
menche number input user''')

n = int(input("Input znachenie poslednego namber Fibonachi: "))

def fib_n_namder (n):
	L = []
	a, b = 0, 1
	
	for _ in range (0, n):
		L += [a]
		a, b = b, a + b
		
		if a > n:
			break

	return L

print(fib_n_namder(n))