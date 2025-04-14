string = str(input("Diga uma palavra: "))
c1 = str(input("Diga um caractere dessa palavra: ")).upper()
c2 = str(input("Diga por qual caractere o anterior digitado será substituído: ")).upper()


nova_string = string.upper().replace(c1, c2)
print(nova_string) 