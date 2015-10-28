print("Program nachodit NOD and NOK")

a = int(input("Input namber a: "))
b = int(input("Input namber b: "))

def lcm(a, b):
	m = a * b
	while a != 0 and b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return m // (a + b)


def nod(a, b):
	while a!=0 and b!=0:
		if a > b:
			a = a % b
		else:
			b = b % a
	return a + b

print("NOD = ", nod(a, b))
print('НОК = ', lcm(a, b))


