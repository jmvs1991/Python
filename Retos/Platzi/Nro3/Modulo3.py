def LetraCapital(cadena):

    cadenaFinal = ''

    if len(cadena) > 0:
        
        primeraLetra = cadena[0]
        resto = cadena[1:]

        cadenaFinal = str(primeraLetra).upper() + str(resto).lower()

    return cadenaFinal

def PuercoLatino(cadena):
    
    cadenaFinal = ''

    if len(cadena) > 0:

        primeraLetra = str(cadena[0]).lower()

        if primeraLetra == 'a' or primeraLetra == 'e' or primeraLetra == 'i' or primeraLetra == 'o' or primeraLetra == 'u':
            
            cadenaFinal = f'{cadena}way'

        else:

            primeraConsonante = ''

            for letra in cadena:

                if primeraConsonante == '' and (str(letra).lower() != 'a' or str(letra).lower() != 'e' or str(letra).lower() != 'i' or str(letra).lower() != 'o' or str(letra).lower() != 'u'):
                    primeraConsonante = str(letra).lower()
                    continue

                cadenaFinal = f'{cadenaFinal}{letra}'

            cadenaFinal = f'{cadenaFinal}{primeraConsonante}ay'

    return cadenaFinal