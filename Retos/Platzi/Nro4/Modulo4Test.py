import Modulo4
import unittest

class CajaNegraTest(unittest.TestCase):
    
    def test_Multiplicar(self):

        numero1 = 2
        numero2 = 2
        decimales = 5
        
        resultado = Modulo4.Multiplicar(numero1, numero2, decimales)
        self.assertEqual(resultado, f'%.{decimales}f' % 4)

if __name__ == "__main__":
    unittest.main()
