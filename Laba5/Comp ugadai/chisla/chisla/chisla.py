chislo = input('Input namber: ')
count = len(chislo)
print ("In your namber sostoit from: " + str(count))
sum = 0
chislo = int(chislo)

for _ in range(count):
	#sum1 = chislo - ((chislo // 10)*10)
	sum += chislo % 10
	chislo //= 10

print ('Summa cifr zadannogochisla = ', sum)