import pytest

import main

lista_para_multiplicar = [
    (2, 3, 6),
    (0, 4, 0),
    (-5, -3, 15),
    (8, 1000, 8000)
]


@pytest.mark.parametrize('num1, num2, resultado_esperado', lista_para_multiplicar)
def teste_multiplicar_2_numeros(num1, num2, resultado_esperado):
    # Configura  -  virá da lista

    # Executa
    resultado_obtido = main.multiplicar_2_numeros(num1, num2)

    # Valida
    assert resultado_esperado == resultado_obtido
