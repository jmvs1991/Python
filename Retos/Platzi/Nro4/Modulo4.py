def Multiplicar(numero1, numero2, decimales = 2):
    try:

        numero1 = float(numero1)
        numero2 = float(numero2)
        decimales = int(decimales)

        decimales = 2 if decimales <= 0 else decimales
    
        resultado = (numero1 * numero2)

        return f'%.{decimales}f' % resultado

    except:

        return 0

def RaizCuadrada(numero):

    try:
        pass
    except:
        pass
