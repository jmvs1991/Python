import Modulo3

try:
        
    repetir = True

    while repetir == True:
        
        print('Reto #1 Longitud del string')
        print('Reto #2 ‘Suma’ de strings')
        print('Reto #3 Ajusta las iniciales')
        print('Reto #4 String fragmentado')
        print('Reto #5 Mayúsculas y minúsculas')
        print('Reto #6 Nombres cortos y largos')
        print('Reto #7 ¡Hablemos Pig Latin! (Puerco Latino) 🐷')

        reto = int(input('¿Que reto desea ejecutar? '))

        if reto == 1:
            
            # Pide a tu usuario que ingrese el nombre de su curso favorito, 
            # obtén la longitud de ese string y muéstralo en pantalla.
            curso = input('¿Cual es tu curso favorito? ').strip()

            print(f'{curso} tiene {len(curso)} letras')

        elif reto == 2:

            # Crea un programa en el que le pidas en 3 variables distintas: 
            # nombre, apellido y comida favorita. 
            # Como salida mostrarás el mensaje Hola, 
            # mi nombres es {nombre} {apellido} y mi comida favorita es {comida} en un solo string.
            
            nombre = input('¿Como te llamas?').strip()
            apellido = input('¿Cual es tu apellido?').strip()
            comida = input('¿Cual es tu comida favorita?').strip()

            print(f'Mi nombre es {nombre} {apellido} y mi comida favorita es {comida}')

        elif reto == 3:

            # Ahora, pedirás a tu usuario que ingrese su nombre, apellido y país de origen en minúsculas. 
            # Después mostrarás los datos de salida con mayúscula inicial al tratarse de nombres propios.
            nombre = input('¿Como te llamas? ')
            apellido = input('¿Cual es tu apellido? ')
            pais = input('¿Cual es tu país de origen? ')

            nombre = Modulo3.LetraCapital(nombre)
            apellido = Modulo3.LetraCapital(apellido)
            pais = Modulo3.LetraCapital(pais)

            print(f'Nombre: {nombre}')
            print(f'Apellido: {apellido}')
            print(f'País: {pais}')

        elif reto == 4:

            # Solicita a tu usuario que indique una oración de 10 o más caracteres, 
            # la línea de un poema o canción funcioona excelente. 
            # Calcula la longitud del string, pide un número de rango inicial y 
            # final que esté entre la longitud del string para al final mostrar el fragmento que incluya 
            # los caracteres en ese intervalo.
            oracion = input('Por favor escriba una oración de 10 o mas caracteres')

            if len(oracion) < 10:
                
                print('La oración debe tener mas de 10 caracteres: ').strip()

            else:

                inicio = input(f'por favor ingrese un valor que este entre 1 y {len(oracion)}')
                fin = input(f'por favor ingrese un valor que este entre {inicio} y {len(oracion)}')

                print(oracion[inicio: fin])

        elif reto == 5:

            # Solicita a tu usuario que indique 2 palabras, 
            # donde al mostrarlas en pantalla una estará totalmente en mayúsculas y otra en minúsculas ¿fácil, no?
            
            palabra1 = input('Escriba la primera palabra: ').strip().lower()
            palabra2 = input('Escriba la segunda palabra: ').strip().upper()

            print(f'Primera palabra: {palabra1}')
            print(f'Segunda palabra: {palabra2}')

        elif reto == 6:

            # Ya sabemos trabajar con nombres ¿pero qué pasa si cumple ciertas cualidades?
            # Tu usuario ingresará su nombre, 
            # si tiene una longitud mayor a 5 caracteres mostrarás un saludo con su nombre en pantalla. 
            # Si tiene menos de 5 caracteres, pedirás su apellido, 
            # mostrarás el saludo con nombre y apellido. 
            # En ambos casos deberás mostrarlos con mayúscula inicial.
            
            nombre = input('Escriba su nombre: ').strip()

            nombre = Modulo3.LetraCapital(nombre)

            if len(nombre) >= 5:
                
                print(f'Hola {nombre}')

            else:
                
                apellido = input('Escriba su apellido: ').strip()
                apellido = Modulo3.LetraCapital(apellido)

                print(f'Hola {nombre} {apellido}')

        elif reto == 7:

            # Espera ¡¿qué?!
            # PuercoLatino es como el idioma de la “efe”, 
            # donde cambiamos las palabras bajo ciertas condiciones. En este caso será así:

            # La primer consonante de una palabra se pasa al final y se agrega la sílaba “ay”.
            # Si una palabra inicia con vocal, se agrega “way” al final.
            # Ejemplos:

            # Platzi 👉 Latzipay
            # Abeja 👉 Abejaway

            palabra = input('Escriba una palabra: ')

            palabra = Modulo3.PuercoLatino(palabra)
            palabra = Modulo3.LetraCapital(palabra)

            print(palabra)

            pass

        else:
            print('El reto indicado no existe')

        repetirStr = input('¿Desea ejecutar otra tarea? Si o No').lower().strip()
        repetir = True if repetirStr == 'si' else False

except:
    print('El valor ingresado no es correcto')

finally:
    print('Presione cualquier tecla para continuar')