
print('''Polzovatel vvodit poryadkovi nomer elementa posledovatelnosti Fibonachi,
 a programma vuvodit znachenie dannogo elementa''')

namber = int(input("Vvedite poryadkovi nomer elementa posledovatelnosti Fibonachi: "))

fib1 = 0
fib2 = 1
schetchik = 0
i = 0

while i < namber - 1 :
	sumFib = fib1 + fib2
	fib1 = fib2
	fib2 = sumFib
	i += 1

if i == namber - 1:
	print(fib1)

else:
	print(fib1)