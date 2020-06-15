def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)

def Rango(desde, hasta, actual, lista = []):

    lista.append(actual)
    creciente = (desde <= hasta)

    if creciente == True:
        
        if actual >= hasta:

            return lista
        
        else:

            return Rango(desde, hasta, actual + 1, lista)

    else:
        
        if actual <= hasta:

            return lista
        
        else:

            return Rango(desde, hasta, actual - 1, lista)

def RangoHasta(n, lista):
    
    lista.append(n)

    if n == 0:
        return lista
    else:
        return RangoHasta(n - 1, lista)

def SumaHasta(tope, actual = 0):

    if tope == actual:
        return actual
    else:
        return actual + SumaHasta(tope, actual + 1)

def RemoverTodos(lista, elemento, posicion = 0, listaFiltrada = []):
    
    if posicion >= len(lista):
        
        return listaFiltrada

    else:
        
        elementoActual = lista[posicion]
        
        if elementoActual != elemento:

            listaFiltrada.append(elementoActual)
        
        return RemoverTodos(lista, elemento, posicion + 1, listaFiltrada)