print("Program nachodit vse prostue deliteli zadannogo namber")

namber = int(input("Input namber: "))
print("Prostue deliteli: ")

while namber > 1:
    x = 2
    y = 0
    while 1:
        if namber % x == 0:
            namber = namber // x
            print(x, end = ' ')
            y = 1
            break
        else:
            x += 1
    if y == 1:
        continue
print()
