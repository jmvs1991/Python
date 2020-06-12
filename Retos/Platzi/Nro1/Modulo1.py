def Saludar(nombre, apellido=''):
    return f'Hola, {nombre} {apellido}'.strip()

def ImprimirCursos(cursos):
    print('Platzi cuenta con cursos de: ')
    for curso in cursos:
        print(curso)

def SumarDosNros(numero1, numero2):
    try:
            
        numero1 = float(numero1)
        numero2 = float(numero2)
        suma = numero1 + numero2

        return suma
        
    except:
        print('Los valores para las sumas tienen que ser numeros')
        return 0

def SumarYMultiplicar(numero1, numero2, numero3):
    try:
            
        numero1 = float(numero1)
        numero2 = float(numero2)
        numero3 = float(numero3)

        suma = (numero1 + numero2) * numero3

        return suma

    except:
        print('Los valores para las sumas tienen que ser numeros')
        return 0

def Dia_A_Horas(dias):

    try:

        dias = int(dias)

        horas = dias * 24

        return horas

    except:
        print('El valor ingresado no es un numero')
        return 0

def Dia_A_Minutos(dias):
    
    try:

        dias = int(dias)

        minutos = dias * 1440

        return minutos

    except:
        print('El valor ingresado no es un numero')
        return 0

def Dia_A_Segundos(dias):
    
    try:

        dias = int(dias)

        segundos = dias * 86400

        return segundos

    except:
        print('El valor ingresado no es un numero')
        return 0

def Millas_A_Kilometros(millas):

    try:

        millas = float(millas)

        kilometros = millas * 1.609344

        return kilometros

    except:

        print('El valor ingresado no es un monto')
        return 0