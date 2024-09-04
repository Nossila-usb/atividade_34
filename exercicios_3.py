# Exercicios 03 :
# Crie um programa onde o usuário informa um número inteiro, e o programa informa se o número e par ou ímpar.


num_digitado = int(input("Digite um Número inteiro: "))
if num_digitado % 2 == 0:
    print(f"O número {num_digitado} é par!")
else:
    print(f"O número {num_digitado} é ímpar!")