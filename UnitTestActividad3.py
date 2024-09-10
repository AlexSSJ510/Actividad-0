import unittest

class Calculadora:
    def calcular(self, multiplicando, multiplicador, sumador):
        result = multiplicando * multiplicador + sumador
        return result

    def potencia(self, base):
        return base ** 2

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_calcular(self):
        # Caso de prueba: multiplicando=2, multiplicador=3, sumador=4
        resultado = self.calculadora.calcular(2, 3, 4)
        self.assertEqual(resultado, 10)  # 2*3 + 4 = 10

        # Caso de prueba: multiplicando=5, multiplicador=0, sumador=7
        resultado = self.calculadora.calcular(5, 0, 7)
        self.assertEqual(resultado, 7)  # 5*0 + 7 = 7

        # Caso de prueba: multiplicando=-2, multiplicador=-3, sumador=-4
        resultado = self.calculadora.calcular(-2, -3, -4)
        self.assertEqual(resultado, 2)  # -2*(-3) + (-4) = 6 - 4 = 2

    def test_potencia(self):
        # Caso de prueba: base=3
        resultado = self.calculadora.potencia(3)
        self.assertEqual(resultado, 9)  # 3**2 = 9

        # Caso de prueba: base=-4
        resultado = self.calculadora.potencia(-4)
        self.assertEqual(resultado, 16)  # (-4)**2 = 16

        # Caso de prueba: base=0
        resultado = self.calculadora.potencia(0)
        self.assertEqual(resultado, 0)  # 0**2 = 0

if __name__ == "__main__":
    unittest.main()