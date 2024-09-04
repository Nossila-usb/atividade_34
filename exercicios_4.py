#  Exercicios 04 :
#  Crie um programa que o usuário informa um número inteiro positivo, e o programa exibe na tela uma contagem regressiva. importação de bibliotecas

import os
import time

numero = int(input('Informe um número inteiro: '))

while numero >= 0:
    os.system('cls')
    print('\nContagem regressiva:')
    print(f'{numero}...')
    numero -= 1
    time.sleep(1)
    
os.system('cls')
print('Kabuuuummmm!!!!\n')