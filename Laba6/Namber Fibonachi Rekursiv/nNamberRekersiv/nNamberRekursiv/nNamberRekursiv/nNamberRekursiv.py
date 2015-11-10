
#программа позволяет вывести n чисел последовательности Фибоначчи

n = int(input("Input kolichestvo namber Fibonachi: "))


def fib_n_namder (n):
	L = []
	a, b = 0, 1
	
	for _ in range (0, n):
		L += [a]
		a, b = b, a + b
		
	return L

print(fib_n_namder(n))
