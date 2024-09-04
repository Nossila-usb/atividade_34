# Exercicios 08:

def media(numeros):
    return sum(numeros) / len(numeros)

numeros = []

while True:
    print(f' MÉDIA ENTRE OS NÚMEROS ')
    print('1 - Adicionar números,')
    print('2 - Calcular a média entre os números.')

    opcao = int(input(' opção desejada: '))

    match opcao:
        case 1:
            novo_num = int(input('Informe o número : '))
            numeros.append(novo_num)
            print(f'Número {novo_num} adicionado com sucesso.')
        case 2:
            print(f'Média da lista: {media(numeros)}')