# Exercios 02 : 
# Crie um programa que receba o peso (em gramas) de um bebê recém-nascido, e indique se o bebê está normal ou se precisa ficar internado, caso o bebê tenha menos que 2500g.

peso_bebe = int(input('Digite o peso do Bebê em gramas: '))
if peso_bebe < 2500:
    print('ATENÇÃO - Recém nascido necessita de Internação!')
else: 
    print('Bebê liberado!')