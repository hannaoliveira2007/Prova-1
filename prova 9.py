x = int(input("Valor 1: "))
y = int(input("Valor 2: "))

if x > y:
    for z in range(y, x + 1):
        if (z % 5 == 2) or (z % 5 == 3):
            print(z)
else:
    for z in range(x, y + 1):
        if (z % 5 == 2) or (z % 5 == 3):
            print(z)