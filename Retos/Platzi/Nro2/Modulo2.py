def Numero_Mayor(numero1, numero2):
    
    resultado = {
        "Diferencia": '',
        "Comparacion": ''
    }

    try:
    
        numero1 = int(numero1)
        numero2 = int(numero2)
        Mensaje = ''
        diferencia = numero1 - numero2

        if diferencia == 0:
            
            Mensaje = 'Los numeros son iguales'
            
        elif diferencia > 0:

            Mensaje = f'El {numero1} es mayor al {numero2} '

        else:
            
            Mensaje = f'El {numero2} es mayor al {numero1} '

        resultado["Diferencia"] = f'la diferencia entre ambos numeros es de {(diferencia * -1) if diferencia < 0 else diferencia}'
        resultado["Comparacion"] = Mensaje

        return resultado

    except:
        return resultado

def Rango(limite, valor):

    try:

        limite = int(limite)
        valor = int(valor)
        
        if valor > limite:
            return f'El número {valor} excede el límite permitido'
        else:
            return f'El número {valor} se encuentra en el rango, gracias.'
        
    except:
        return 'Los valores indicados no son correctos'

def Rando_Doble(limiteInf, limiteSup, valor):

    try:
        
        limiteInf = int(limiteInf)
        limiteSup = int(limiteSup)
        valor = int(valor)

        if valor > limiteInf and valor < limiteSup:
            return f'El {valor} se encuentra entre los limites [{limiteInf},{limiteSup}].'
        elif valor < limiteInf:
            return f'El {valor} se encuentra por debajo del limite inferior [{limiteInf}]'
        elif valor > limiteSup:
            return f'El {valor} se encuentra por encima del limite superior [{limiteSup}]' 
        
    except:
        return 'Los valores indicados no son correctos'