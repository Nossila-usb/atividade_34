# Exercicios 07: 

nomes = []

while True:
    print(f'LISTA DE NOMES')
    print('1 - Inserir nome na lista.')
    print('2 - Exibir lista de nomes.')
    print('3 - Sair do programa.')

    opcao = input(' opção desejada: ')

    try:
        match opcao:
            case '1':
                novo_nome = input('Informe novo nome na lista: ')
                nomes.append(novo_nome)
                print(f'Novo nome {novo_nome} inserido com sucesso.')
                continue
            case '2':
                nomes.sort()
                for i in nomes:
                    print(i)
            case '3':
                print('Programa encerrado.')
                break
            case _:
                    print('Opção não encontrada.\n')
                    continue
    except:
        print('Indíce não encontrado.')
        continue