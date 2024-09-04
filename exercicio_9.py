# Exercicios 09:
#mportar biblioteca
from datetime import date 

evento = []
classificacao = []


data = f'{date.today().day}/{date.today().month}/{date.today().year}'

while True:
    print(f' EVENTOS ')
    print('1 - Cadastrar novo evento.')
    print('2 - Lista de eventos.')
    print('3 - Participar de algum evento.')
    print('4 - Sair do programa.')

    opcao = int(input('Informe opção desejada: '))

    try:
        match opcao:
            case 1:
                nome_evento =input('Informe o nome do evento: ')
                evento.append(nome_evento)
                nova_classificacao = input('Informe classificação do filme: ')
                classificacao.append(nova_classificacao)
                print(f'Evento: {nome_evento} Classificação: {nova_classificacao}')
                continue
            case 2:
                    for evt, clsf in zip(evento, classificacao):
                        print(f'Evento: {evt} - Classificação: {clsf}')
                        continue
            case 3:
                nome = input('Informe seu seu nome: ')
                idade = int(input('Informe sua idade: '))

                evento_escolhido = input('Informe o evento desejado: ')

                if evento_escolhido in evento:
                    indice_evento = evento.index(evento_escolhido)
                    classif_evento = classificacao[indice_evento]


                    if idade >= int(classif_evento):
                        print('\n')
                        print(f'Ingresso impresso no dia: {data}')
                        print(f'Pagante: {nome}.')
                        print(f'Evento: {evento_escolhido}.')
                        break
                    else:
                        print(f'{nome} não possui a idade mínima para participar do evento: {evento_escolhido}.')
                        print('Favor, escolher outro evento.')
                        continue
                else:
                    print(f'O evento {evento_escolhido} não foi encontrado.')
                    continue
            case 4:
                print('Programa encerrado.')
                break
    except:
        print('Opção informada não é valida.')
                




