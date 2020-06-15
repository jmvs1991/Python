import RecursividadModulo
import IteracionModulo

def Recursividad():
    try:
    
        repetir = True

        while repetir == True:
        
            print('Recursividad #1 - Factorial')
            print('Recursividad #2 - Rango desde-hasta')
            print('Recursividad #3 - Rango hasta')
            print('Recursividad #4 - Suma hasta')
            print('Recursividad #5 - Remover todos')
                        
            reto = int(input('¿Que reto desea ejecutar? '))

            if reto == 1:

                numero = int(input('Indique un numero: '))

                factorial = RecursividadModulo.Factorial(numero)

                print(f'El factorial de {numero} es {factorial}')

            elif reto == 2:

                """
                    rango(desde, hasta) -> lista de números: similar a rango, 
                    pero ahora se puede especificar el "desde". 
                    Ej: rango(5, 10) -> [5,6,7,8,9,10]. 
                    No hace falta validar que desde sea menor a hasta o tener rangos decrecientes.
                """

                desde = int(input('Indique el rango inicial: '))
                hasta = int(input('Indique el rango final: '))
                actual = desde

                Lista = RecursividadModulo.Rango(desde, hasta, actual, [])

                print(Lista)

            elif reto == 3:

                """
                    rangoHasta(n) -> Lista de números: 
                    dado un número "n", retorna la lista de números desde el 0 hasta el N incluído. 
                    Por ejemplo: rangoHasta(5) -> [0,1,2,3,4,5].
                """

                numero = int(input('Indique un numero: '))

                ListaFinal = RecursividadModulo.RangoHasta(numero, [])

                print(ListaFinal)    

            elif reto == 4:

                """
                    sumaHasta(n) -> numero. 
                    Retorna la suma de los numeros desde el 0 hasta el N. Por ejemplo. 
                    sumaHasta(5) = 5 + 4 + 3 + 2 + 1 + 0 => 15
                """

                numero = int(input('Indique un numero: '))
                suma = RecursividadModulo.SumaHasta(numero, 0)
                print(f'La sumatoria es {suma}')

            elif reto == 5:

                """
                    removerTodos(lista, elemento): -> lista, Dada una lista y un elemento, 
                    retorna otra lista igual a la original, 
                    pero sin el "elemento" dado. 
                    En caso en que el elemento aparezca múltiples veces, lo remueve de todas. 
                    Ejemplo: remover([1,2,3,1,6,7,1,9,1], 1) -> [2,3,6,7,9]
                """

                lista = [1,2,3,1,6,7,1,9,1]
                elemento = int(input(f'Que elemento quiere remover de la siguiente lista {lista}'))

                ListaFiltrada = RecursividadModulo.RemoverTodos(lista, elemento, 0, [])

                print(ListaFiltrada)

            else:
                print('El reto indicado no existe')
        
            repetirStr = input('¿Desea ejecutar otra tarea? Si o No').lower().strip()

            repetir = True if repetirStr == 'si' else False

    except:
        print('El valor ingresado no es correcto')

def Iteracion():
    try:
        
        repetir = True

        while repetir == True:

            print('Iteración #1 - Factorial')
            print('Iteración #2 - Rango desde-hasta')
            print('Iteración #3 - Rango hasta')
            print('Iteración #4 - Suma hasta')
            print('Iteración #5 - Remover todos')
                        
            reto = int(input('¿Que reto desea ejecutar? '))

            if reto == 1:
                
                numero = int(input('Indique un numero: '))

                factorial = IteracionModulo.Factorial(numero)

                print(f'El factorial de {numero} es {factorial}')

            elif reto == 2:

                """
                    rango(desde, hasta) -> lista de números: similar a rango, 
                    pero ahora se puede especificar el "desde". 
                    Ej: rango(5, 10) -> [5,6,7,8,9,10]. 
                    No hace falta validar que desde sea menor a hasta o tener rangos decrecientes.
                """

                desde = int(input('Indique el rango inicial: '))
                hasta = int(input('Indique el rango final: '))
                
                Lista = IteracionModulo.Rango(desde, hasta)

                print(Lista)

            elif reto == 3:

                """
                    rangoHasta(n) -> Lista de números: 
                    dado un número "n", retorna la lista de números desde el 0 hasta el N incluído. 
                    Por ejemplo: rangoHasta(5) -> [0,1,2,3,4,5].
                """

                numero = int(input('Indique un numero: '))

                ListaFinal = IteracionModulo.RangoHasta(numero)

                print(ListaFinal) 

            else:

                print('El reto indicado no existe')
            
            repetirStr = input('¿Desea ejecutar otra tarea? Si o No').lower().strip()

            repetir = True if repetirStr == 'si' else False
        
    except:
        print('El valor ingresado no es correcto')

if __name__ == "__main__":
    
    try:
    
        repetir = True

        while repetir == True:
            
            print('Recursividad Vs Itereción')
            print('#1 Ver Recursividad')
            print('#2 Ver Iteración')

            opcion = int(input('¿Que opcion desea ejecutar? '))

            if opcion == 1:

                Recursividad()

            elif opcion == 2:

                Iteracion()

            else:
                print('La opción no es válida')
        
            repetirStr = input('¿Desea ejecutar otra opción? Si o No').lower().strip()

            repetir = True if repetirStr == 'si' else False

    except:
        print('El valor ingresado no es correcto')

    finally:
        print('Presione cualquier tecla para continuar')