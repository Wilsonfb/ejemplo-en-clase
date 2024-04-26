#Crear una clase estudiante que tenga los atributos nombre, edad y grado y que los pidan.

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
nombre=input("Digite su nombre: ")
edad=input("Digite su edad: ")
curso=input("Digite su curso: ")
Estudiante=(nombre, edad, curso)
print(f"Su nombre es {nombre} tiene {edad} años y esta en {curso}.")