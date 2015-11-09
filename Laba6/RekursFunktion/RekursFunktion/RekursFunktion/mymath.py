def pow(x, n):
	y = x

	# вычисление функции x^n
	for _ in range(n - 1):
		y = y * x

	return y

	# вычисление функции x^n другим способом
def pow2(x, n):
	if n == 0:
		return 1
	else:
		return x * pow2(x, n - 1)

	# вычисление функции n!
def faktorial(n):

	if n == 0:
		return 1

	return n * faktorial(n - 1)