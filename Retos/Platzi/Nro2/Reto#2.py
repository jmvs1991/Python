import Modulo2

try:
    
    repetir = True

    while repetir == True:
    
        print('Reto #1 - Número mayor y menor')
        print('Reto #2 - En el rango, por favor.')
        print('Reto #3 - Rangos cambiantes.')
        print('Reto #4 - “I like turtles”')
        print('Reto #5 - ¿Cómo está el clima?')
        print('Reto #6 - Edad permitida')
        print('Reto #7 - Mensajes opcionales')
        
        reto = int(input('¿Que reto desea ejecutar? '))

        if reto == 1:

            numero1 = input('indique un numero: ')
            numero2 = input('indique otro numero: ')

            resultado = Modulo2.Numero_Mayor(numero1, numero2)

            print(resultado.get('Diferencia'))
            print(resultado.get('Comparacion'))

        elif reto == 2:

            limite = input('Indique el limite: ')
            valor = input('Indique el valor: ')

            resultado = Modulo2.Rango(limite, valor)

            print(resultado)

        elif reto == 3:

            limiteInf = input('Limite inferior: ')
            limiteSup = input('Limite superior: ')
            valor = input('Valor: ')

            resultado = Modulo2.Rando_Doble(limiteInf, limiteSup, valor)

            print(resultado)

        elif reto == 4:

            animalStr = input('¿Cual es tu anímal favorito?').lower().strip()

            if animalStr == 'tortuga':
                print('También me gustan las tortugas')
            else:
                print('Ese animal es genial, pero prefiero las tortugas')

        elif reto == 5:

            # Crea un programa que pregunte al usuario si está lloviendo, en caso de responder “sí” 
            # pregunta si está haciendo mucho viento y si responde “sí” nuevamente muestra un mensaje 
            # indicando que hace mucho viento para salir con una sombrilla. En caso contrario, 
            # anima al usuario a que lleve una sombrilla. 
            # Para el caso de responder “no” en la primer pregunta, entonces solo desea un bonito día.
            # Considera que las respuestas pueden pasarse a minúsculas para evitar posibles errores.

            lloviendoStr = input('¿Esta lloviendo? Sí o No ').lower().strip()
            lloviendo = True if lloviendoStr == 'sí' or lloviendoStr == 'si' else False

            if lloviendo == True:

                vientoStr = input('¿está haciendo mucho viento? Sí o No').lower().strip()
                viento = True if vientoStr == 'sí' or vientoStr == 'si' else False

                if viento == True:
                    print('Hace mucho viento para salir con una sombrilla')
                else:
                    print('Deberías llevar una sombrilla')

            else:

                print('Que tengas un boníto día')

        elif reto == 6:

            #Pide al usuario que ingrese su edad y mostrarás un mensaje correspondiente 
            # si esta coincide con las siguientes condiciones:
            # Más de 30 años: Nunca es tarde para aprender ¿Qué curso tomaremos?
            # Entre 29 y 18 años: Es un momento excelente para impulsar tu carrera.
            # Menos de 18 años: ¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.

            edad = int(input('¿Que edad tienes?'))

            if edad > 30:
                print('Nunca es tarde para aprender ¿Qué curso tomaremos?')
            elif edad >= 18 and edad <= 29:
                print('Es un momento excelente para impulsar tu carrera.')
            else:
                print('¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.')

        elif reto == 7:

            # Crearás un un script para el que el usuario indicará un número entre 1 y 6. 
            # Como respuesta se le brindará un mensaje según el número leido:
            # 1 - “Hoy aprenderemos sobre prorgamación”
            # 2 - “¿Qué tal tomar un curso de marketing digital?
            # 3 - “Hoy es un gran día para comenzar a aprender de diseño”
            # 4 - ¿Y si aprendemos algo de negocios online?
            # 5 - “Veamos un par de clases sobre producción audiovisual”
            # 6 - “Tal vez sea bueno desarrollar una habilidad blanda en Platzi”
            # En caso indicar un número distinto, pedir al usuario que ingrese uno en el rango válido.

            repetir = True

            while repetir == True:

                try:

                    numero = int(input('Indique un nro del 1 al 6: '))

                    if numero < 1 or numero > 6:
                        
                        repetir = True
                        print('Por favor intente nuevamente con un numero válido')

                    elif numero == 1:

                        print('Hoy aprenderemos sobre prorgamación')
                        repetir = False

                    elif numero == 2:

                        print('¿Qué tal tomar un curso de marketing digital?')
                        repetir = False

                    elif numero == 3:

                        print('Hoy es un gran día para comenzar a aprender de diseño')
                        repetir = False

                    elif numero == 4:
                    
                        print('¿Y si aprendemos algo de negocios online?')
                        repetir = False

                    elif numero == 5:

                        print('Veamos un par de clases sobre producción audiovisual')
                        repetir = False

                    else:

                        print('Veamos un par de clases sobre producción audiovisual')
                        repetir = False
                    
                except:

                    print('El valor indicado no es un nro.')
                    repetir = True

        else:
            print('El reto indicado no existe')
    
        repetirStr = input('¿Desea ejecutar otra tarea? Si o No').lower().strip()

        repetir = True if repetirStr == 'si' else False

except:
    print('El valor ingresado no es correcto')

finally:
    print('Presione cualquier tecla para continuar')