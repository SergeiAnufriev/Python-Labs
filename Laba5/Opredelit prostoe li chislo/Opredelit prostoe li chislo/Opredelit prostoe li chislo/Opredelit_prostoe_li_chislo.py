def isNatural(n):
	# ������� ������ ������ ��� �������� ������� �����
	lst = []
	# � k ����� ������� ���������� ���������
	k = 0
	# ��������� ��� ����� �� 2 �� N
	for i in range(2, n + 1):
		# ��������� ��� ����� �� 2 �� ��������
		for j in range(2, i):
			# ���� ���������� ���������
			if i % j == 0:
				k = k + 1
		# ���� ��������� ���, ��������� ����� � ������
		if k == 0:
			lst.append(i)
		else:
			k = 0

	if n in lst:
		return True
	else:
		return False


n = int(input("n="))

if (isNatural(n)):
	print("natural")
else: 
	print("not natural")
