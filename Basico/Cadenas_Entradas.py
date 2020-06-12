my_str = input('¿Cual es tu nombre? ')
my_str_end = f'Hola {my_str}'
print(my_str_end)
print(f'La longitud de la cadena es {len(my_str_end)}')

'''
    El slice de cadenas tiene el siguiente formato
    cadena[start, end, step]
'''

print(f'{type(my_str)}')
print(f'Longitud: {len(my_str)}')
print(f'Primera letra: {my_str[0]}')
print(f'{my_str[::2]}')
print(f'{my_str[2:]}')

input('Terminado')