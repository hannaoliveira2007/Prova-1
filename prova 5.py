qtd_alunos = int(input("Qual a quantidade de alunos? "))
notas = []

while True:
    entrada = input("Digite a nota (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        nota = float(entrada)
        if nota >= 0:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor positivo.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'sair'.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("A média da turma é:", media)
else:
    print("Nenhuma nota válida foi inserida.")

acima = media*1.1
abaixo = media*0.9

notas_acima = [n for n in notas if n > acima ]
notas_abaixo = [n for n in notas if n < abaixo ]

print("\nNotas 10% acima da média: ", notas_acima)
print("Notas 10% abaixo da média: ", notas_abaixo)