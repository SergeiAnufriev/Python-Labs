
print('''Polzovatel vvodit poryadkovi nomer elementa posledovatelnosti Fibonachi,
 a programma vuvodit znachenie dannogo elementa''')

n = int(input("Vvedite poryadkovi nomer elementa posledovatelnosti Fibonachi: "))

def fib(n, a = 0, b = 1):
	if n == 0:
		return a
	else:
		return fib(n - 1, b, a + b)

print (fib(n))