class Persona:
    def __init__(self,  nombre, edad):
        self.__nombre = nombre   #Atributo privado doble guion de subrayado
        self.__edad = edad   #Atributo privado doble guion de subrayado
    def get_nombre(self):
        return self.__nombre #Metodo para obtener el valor del atributo privado
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre # Metodo  para MODIFICAR  el valor del atributo
    def get_edad(self):
        return self.__edad #Metodo para obtener el valor del atributo privado
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad # Metodo  para MODIFICAR  el valor del atributo
# Ejemplo 1
persona1 = Persona("IVAN", 18) # creamos un objeto de la clase Persona con Valores
print(persona1.get_nombre()) # Salida: IVAN -- Obtenemos el nombre mediante el metodoalida
print(persona1.get_edad()) # Salida: 18 -- Obtenemos el nombre mediante el metodoalida
# print(persona1.__nombre)  --> genera error
persona1.set_nombre("Katerine") #Modificamos el nombre de lapersona a travez del metodo set_nombre()
persona1.set_edad(17) #Modificamos la edad  de lapersona a travez del metodo set_nombre()
print(persona1.get_nombre()) #Salida Katerine  que es el nuevo nombre
print(persona1.get_edad()) #Salida 17  que es el nuevo nombre