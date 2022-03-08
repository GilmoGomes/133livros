import unittest

import main


class MyTestCase(unittest.TestCase):
    def testar_soma_2_numeros(self):
        resultado_esperado = 10
        resultado_obtido = main.somar_2_numeros(5, 5)
        self.assertEqual(resultado_obtido, resultado_esperado)  # add assertion here



if __name__ == '__main__':
    unittest.main()
