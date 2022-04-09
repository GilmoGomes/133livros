def dizer_oi(nome):
    print(f'Ola, {nome}')


def somar_2_numeros(num1, num2):
    return num1 + num2


def multiplicar_2_numeros(num1, num2):
    return num1 * num2


def dividir_2_numeros(num1, num2):
    try:             # tente fazer a conta
        return num1 / num2
    except ZeroDivisionError:
        return 'divisao por zero'

def calcular_area_quadrado(lado):
    return lado * lado

def calcular_area_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_triangulo(largura, comprimento):
    return (largura * comprimento) / 2





if __name__ == '__main__':  # accordion da execução do script
    dizer_oi('Gilmo Gomes')
    '''
    somar_2_numeros(2, 3)
    num1 = 17.10
    num2 = 19.90
    resultado = somar_2_numeros(num1, num2)
    print(f'A Soma de {num1} e {num2} é igual a {resultado}')
    print(f'{num1}+{num2}={resultado}')
    print(f'O resultado é {resultado}')
    '''
    # Soma
    resultado = somar_2_numeros(20, 30)
    print(f'O resultado da soma é {resultado}')

    # Multiplicacao

    resultado = multiplicar_2_numeros(3, 5)
    print(f'O resultado da multiplicacao é {resultado}')

    # Divicao
    resultado = dividir_2_numeros(8, 4)
    print(f'O resultado da divisao é {resultado}')

