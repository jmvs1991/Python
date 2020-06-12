class Persona:

    def __init__(self, nombre, edad):
        # con el __ se declara como privado
        self.__Nombre = nombre
        self.__Edad = edad

    @property
    def Nombre(self):
        return self.__Nombre

    @property
    def Edad(self):
        return self.__Edad

    @Nombre.getter
    def Nombre(self):
        return self.__Nombre

    @Edad.setter
    def Edad(self, edad):
        self.__Edad = edad

    def Saludar(self):
        print(f'Hola me llamo {self.__Nombre} y tengo {self.__Edad} años')

#Clase con Herencia
class Hijo(Persona):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def EsMayor(self):
        if self.Edad >= 18:
            return True
        else:
            return False
    
    #Polimorfismo
    def Saludar(self):
        return print(f'Hola me llamo {self.Nombre} tengo { self.Edad } y soy {"Mayor de edad" if self.EsMayor() == True else "Menor de edad"}')

# persona = Persona('Jose', 28)
# persona.Edad = 30
# persona.Saludar()
# print(persona.Nombre)
# print(persona.Edad)

hijo = Hijo('Manuel', 15)
hijo.Saludar()
print(hijo.EsMayor())
print(hijo.Nombre)
print(hijo.Edad)