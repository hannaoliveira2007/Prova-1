palavra = input("Digite uma palavra: ")
arvalap = " "

for x in range(len(palavra) -1, -1, -1):
    arvalap += palavra[x]

print(arvalap)