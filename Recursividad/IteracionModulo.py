def Factorial(n):

    #!5 = 5 * 4 * 3 * 2 * 1 => 120
    calculoFactorial = 1

    for jv in range(1, n + 1):
        calculoFactorial = calculoFactorial * jv
        
    return calculoFactorial

def Rango(desde, hasta):

    """
        rango(desde, hasta) -> lista de números: similar a rango, 
        pero ahora se puede especificar el "desde". 
        Ej: rango(5, 10) -> [5,6,7,8,9,10]. 
        No hace falta validar que desde sea menor a hasta o tener rangos decrecientes.
    """
    lista = []
    creciente = (desde <= hasta)
    inicioRango = 0
    finRango = 1

    if creciente == True:
        
        inicioRango = desde
        finRango = hasta + 1
        
    else:
        
        inicioRango = hasta
        finRango = desde + 1
    
    for actual in range(inicioRango, finRango):
        lista.append(actual)

    return lista

def RangoHasta(n):
    
    lista = []

    for jv in range(n + 1):
        lista.append(jv)

    return lista