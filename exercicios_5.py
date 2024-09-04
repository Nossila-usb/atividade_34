# Exercicios 05 :

# Crie uma lista de 10 nomes (informados dentro do programa). Em seguida, o usuário informa um número inteiro equivalente a um índice, e o programa retorna o nome equivalente ao índice
#  informado pelo usuário.

nomes = ['Bruno', 'Alessandro', 'Daniel', 'Victor', 'Rafael', 'Bruna', 'Alessandra', 'Daniela', 'Vitoria', 'Rafaela']
ind = int(input('Digite um número de 0 a 10 correspondente ao índice do nome a ser exibido: '))
print(f'O nome correspondente ao índice {ind} é: {nomes[ind]}!')