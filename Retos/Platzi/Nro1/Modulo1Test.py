import Modulo1
import unittest

class CajaNegraTest(unittest.TestCase):
    
    def test_Saludo_Nombre(self):

        nombre = 'Jose'

        resultado = Modulo1.Saludar(nombre)

        self.assertEqual(resultado, f'Hola, {nombre}')
    
    def test_Saludo_Nombre_Apellido(self):

        nombre = 'Jose'
        apellido = 'Vasquez'

        resultado = Modulo1.Saludar(nombre, apellido)

        self.assertEqual(resultado, f'Hola, {nombre} {apellido}')

    def test_Sumar_Dos_Numeros(self):

        numero1 = 10
        numero2 = 30

        resultado = Modulo1.SumarDosNros(numero1, numero2)

        self.assertEqual(resultado, (numero1 + numero2))

    def test_Sumar_Dos_Numeros_Y_Multiplicar(self):

        numero1 = 20
        numero2 = 30
        numero3 = 2

        resultado = Modulo1.SumarYMultiplicar(numero1, numero2, numero3)

        self.assertEqual(resultado, (numero1 + numero2) * numero3)

    def test_Dias_A_Horas(self):
        
        dias = 2

        resultado = Modulo1.Dia_A_Horas(dias)

        self.assertEqual(resultado, 48)
    
    def test_Dias_A_Minutos(self):
        
        dias = 2

        resultado = Modulo1.Dia_A_Minutos(dias)

        self.assertEqual(resultado, 2880)

    def test_Dias_A_Segundos(self):
        
        dias = 2

        resultado = Modulo1.Dia_A_Segundos(dias)

        self.assertEqual(resultado, 172800)

    def test_Millas_A_Kilometros(self):

        millas = 5

        resultado = Modulo1.Millas_A_Kilometros(millas)

        self.assertEqual(resultado, 8.04672)

if __name__ == '__main__':
    unittest.main()