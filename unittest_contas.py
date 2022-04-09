# 1 - Bibliotecas
import unittest  # Essa biblioteca será baixada automaticamente pelo PIP

import main  # referencia ao arquivo main.py
# oi

# 2 - Classes (Grupo de definitions(def))
class Casos_De_Teste(unittest.TestCase):
    # 3 - Métodos e Funções
    lista_para_multiplicar = [
        (2, 3, 6),
        (0, 4, 0),
        (-5, -3, 15)
    ]

    def teste_multiplicar_2_numeros(self):
        # A - Configura
        num1 = 2
        num2 = 3
        resultado_esperado = 6

        # B Executa
        resultado_obtido = main.multiplicar_2_numeros(num1, num2)

        # C - Valida
        self.assertEqual(resultado_esperado, resultado_obtido)  # add assertion here

    def teste_somar_2_numeros(self):
        num1 = 7
        num2 = 8
        resultado_esperado = 15

        resultado_obtido = main.somar_2_numeros(num1, num2)

        self.assertEqual(resultado_esperado, resultado_obtido)

    def teste_dividir_2_numeros(self):
        num1 = 25
        num2 = 5
        resultado_esperado = 5

        resultado_obtido = main.dividir_2_numeros(num1, num2)

        self.assertEqual(resultado_esperado, resultado_obtido)


if __name__ == '__main__':
    unittest.main()
