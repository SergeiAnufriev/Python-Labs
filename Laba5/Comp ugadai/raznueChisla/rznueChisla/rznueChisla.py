print("Programma nachodit colichestvo razlichnuch namder v zadannom chisle")

chislo = input('Input namber: ')
count = len(chislo)
print ("In your namber sostoit from: " + str(count))

chislo = int(chislo)

strb = str(chislo % 10)

#for _ in range(count-1):
	
#	chislo //= 10
#	s = str(chislo % 10)

#	if s not in strb:
#		strb += s;

#print("Resalt: " + str(len(strb)))

for _ in range(count-1):
	
	chislo //= 10
	s = str(chislo % 10)
	
	if s not in strb:
		s = int(s)
		strb = int(srtb)

		if s > strb:
			strb = s;

print("Resalt: " + str(strb))