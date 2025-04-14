string = input("Diga uma palavra: ")
c = input("Caractere a ser procurado: ")

o = string.count(c)

if o == 0:
    print("-1")
else:
    print(o)
