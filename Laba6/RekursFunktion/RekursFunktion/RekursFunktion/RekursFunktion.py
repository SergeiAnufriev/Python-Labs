import mymath

def f(x, n):
	
	return mymath.pow(x, n) / mymath.faktorial(n)

print("Program rekursivnoi funttion, vuchislyoychay velichinu x^n/n")

x = int(input("Input x: "))
n = int(input("Input n: "))

print(f(x, n))

