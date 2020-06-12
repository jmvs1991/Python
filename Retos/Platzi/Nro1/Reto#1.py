import Modulo1

try:
       
    repetir = True

    while repetir == True:

        print('Reto #1 “Hola Mundo”')
        print('Reto #2 “Hola… nombre y apellido:”')
        print('Reto #3 “Mensaje multilínea”')
        print('Reto #4 “Suma de enteros”')
        print('Reto #5 “Suma y multiplicación”')
        print('Reto #6 “Resta de pizzas”')
        print('Reto #7 “Edad futura y pasada”')
        print('Reto #8 “Divide la cuenta”')
        print('Reto #9 “Calculando días”')
        print('Reto #10 “Conversor de millas”')
        print('Reto #11 “Cuantas veces un número en otro”')
        
        reto = int(input('¿Que reto desea ejecutar? '))

        if reto == 1:  
            
            nombre = input('¿Como te llamas? ')
            saludo = Modulo1.Saludar(nombre)
            print(saludo)

        elif reto == 2:
            
            nombre = input('¿Como te llamas? ')
            apellido = input('¿Cual es tu apellido? ')
            saludo = Modulo1.Saludar(nombre, apellido)
            print(saludo)

        elif reto == 3:

            cursos = ['Curso1', 'Curso2', 'Curso3']
            Modulo1.ImprimirCursos(cursos)

        elif reto == 4:
        
            numero1 = input('ingrese el primer numero: ')
            numero2 = input('ingrese el segundo numero: ')

            suma = Modulo1.SumarDosNros(numero1, numero2)

            print(f'La suma de ambos numeros es: {suma}')
            print(f'Decimales: { suma % 1 }')
        
        elif reto == 5:
        
            numero1 = input('ingrese el primer numero: ')
            numero2 = input('ingrese el segundo numero: ')
            numero3 = input('ingrese el tercer numero: ')

            suma = Modulo1.SumarYMultiplicar(numero1, numero2, numero3)

            print(f'La suma de ambos numeros es: {suma}')
            print(f'Decimales: { suma % 1 }')

        elif reto == 6:

            rebanadasPizza = int(input('¿Cuantas rebanadas de pizzas hay? '))
            rebanadasDisponibles = rebanadasPizza
            rebanadasConsumidas = 0

            while rebanadasDisponibles > 0:
                
                quiereUnaRebanada = input('¿Quieres tomar una rebanada? Si o No ').lower().strip()

                if quiereUnaRebanada == 'si':
                    rebanadasDisponibles-=1

                rebanadasDisponibles-=1

                print('Alguien mas tomo un pedazo de pizza')
                print(f'Quedan { 0 if rebanadasDisponibles < 0 else rebanadasDisponibles }, la felicidad se acaba con cada segundo que pasa ')

        elif reto == 7:

            nombre = input('¿Como te llamas? ')
            edad = int(input('¿Cuantos años tienes? '))
            edadPasada = edad - 1
            edadFuturo = edad + 1

            print(f'Hola { nombre }, el año pasado tenías { edadPasada } años y el próximo año cumplirás { edadFuturo } años')

        elif reto == 8:

            totalPagar = float(input('¿Cuanto es el total a pagar? '))
            cantidadPersonas = int(input('¿Cuantas personas son?'))
            propina = float(input('Propina: '))
            impuestos = float(input('Impuestos: '))

            propina = (propina / 100)
            impuestos = (impuestos / 100)

            totalPropina = totalPagar * propina
            totalImpuesto = totalPagar * impuestos

            totalGeneral = totalPagar + totalPropina + totalImpuesto
            totalPorPersona = totalGeneral / cantidadPersonas

            print(f'El total a pagar es de {totalGeneral}')
            print(f'El total a pagar por persona es de {totalPorPersona}')

        elif reto == 9:

            dias = input('Indique una cantidad de días ')

            horas = Modulo1.Dia_A_Horas(dias)
            minutos = Modulo1.Dia_A_Minutos(dias)
            segundos = Modulo1.Dia_A_Segundos(dias)

            print(f'Hay { horas } horas en { dias } días')
            print(f'Hay { minutos } minutos en { dias } días')
            print(f'Hay { segundos } segundos en { dias } días')

        elif reto == 10:

            millas = input('Indique una cantidad de millas: ')

            kilometros = Modulo1.Millas_A_Kilometros(millas)

            print(f'{millas} millas son { kilometros } kilometros ')

        elif reto == 11:
            pass

        else:
            print('El reto indicado no existe')
    
        repetirStr = input('¿Desea ejecutar otra tarea? Si o No').lower().strip()

        repetir = True if repetirStr == 'si' else False

except:
    print('El dato introducido es incorrecto')

finally:
    print('Presione cualquier tecla para continuar')
