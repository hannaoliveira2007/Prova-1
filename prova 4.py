x = int(input("Digite um número inteiro: "))
m = 0

for z in range(2, x):
    if (x % z == 0):
      m += 1

if m == 0:
   print("é um número primo")
else:
   print("Não é um número primo")