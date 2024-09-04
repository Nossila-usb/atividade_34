def cal_quadrado(l):
    area_quad = l ** 2
    return area_quad

def cal_circulo(r):
    area_cir = 3.14 * r ** 2
    return area_cir

def cal_triangulo(b,h):
    area_triang = (b * h)/ 2
    return area_triang

def cal_trapezio(B,b,h):
    area_trapez = ((B + b)*h) / 2
    return area_trapez

try: 
    while True:
        print(f'CALCULAR ARÉAS DE FIGURAS GEOMETRICAS')
        print('1 - Calcular área do quadrado.')
        print('2 - Calcular área do círculo.')
        print('3 - Calcular área do triângulo.')
        print('4 - Calcular área do trapézio.')
        print('5 - Sair do Programa.')

        opcao = int(input('Informe opção desejada: '))

        match opcao:
            case 1:
                lados_quadrado = float(input('Informe o cumprimento do lado do quadrado: '))

                area_resultado = cal_quadrado(lados_quadrado)

                print(f'A área do quadrado é {area_resultado} unidades quadradas.')
                continue
            case 2:
                r_circulo = float(input('Informe o raio do círculo: '))

                area_res_cir = cal_circulo(r_circulo)

                print(f'A área do circulo com raio de {r_circulo} é {area_res_cir} cm ao quadrado.')
                continue
            case 3:
                base_triang = float(input('Informe base do triângulo: '))
                altura_triang = float(input('Informe altura do triângulo: '))

                area_cal_triang = cal_triangulo(base_triang,altura_triang)

                print(f'A área do triângulo com base {base_triang} e altura {altura_triang} é: {area_cal_triang} cm ao quadrado.')
                continue
            case 4:
                base_maior_trapz = float(input('Informe a base maior do trapézio: '))
                base_menor_trapz = float(input('Informe base menor do trapézio: ')) 
                altura_trapz = float(input('Informe altura do trapézio: '))

                area_cal_trapezio = cal_trapezio(base_maior_trapz,base_menor_trapz,altura_trapz)

                print(f'A área do trapézio com a base maior {base_maior_trapz}, base menor {base_menor_trapz} e altura {altura_trapz} é: {area_cal_trapezio} cm ao quadrado.')
                continue
            case 5:
                print('Programa encerrado.')
                break
            case _:
                print('Opção desejada não encontrada.')
                continue
except:
    print('Opção inválida.')