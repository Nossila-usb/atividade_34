# Exercicios 06 :
# Crie um programa que possua uma lista com números de 1 a 20, e informe quais deles são primos.
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

if __name__ == '__main__':
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # Lista de números de 1 a 20
    primos = [num for num in numeros if primo(num)]

    print("Números primos de 1 a 20:")
    for primo_num in primos:
        print(primo_num)