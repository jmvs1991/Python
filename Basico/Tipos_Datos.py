"""

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, by

"""

nombre = 'jose'
edad = int(20)
estatura = float(178.5)
print(f'Hola, me llamo {nombre} tengo {edad} años y mido {estatura}')

complejo = complex(1j)

#Las listas son mutables
lista = list(('Manzana', 'Pera', 'Piña'))
print(lista)

#Las tuplas son inmutables
tupla = tuple(('Manzana', 'Pera'))
print(tupla)

rango = range(6)
print(rango)

diccionario = dict(nombre=nombre, edad=edad, estatura=estatura)
print(diccionario)