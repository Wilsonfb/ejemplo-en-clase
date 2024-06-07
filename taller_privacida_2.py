class Persona:
    def __init__(self,  nombre, edad):
        self.__nombre = nombre
        self.__edad = edad   
    def get_nombre(self):
        return self.__nombre 
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre 
    def get_edad(self):
        return self.__edad 
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad
class Estudiante(Persona): 
    def __init__(self, nombre, edad, grado): 
        Persona.__init__(self, nombre, edad)
        self.__grado = grado
    def get_grado(self):
        return self.__grado
    def set_grado(self,nuevo_grado):
        self.__grado = nuevo_grado 
persona1 = Persona("IVAN", 18) 
print(persona1.get_nombre())
print(persona1.get_edad()) 
print("________________________________")
persona1.set_nombre("Katerine")
print(persona1.get_nombre()) 
persona1.set_edad(17) 
print(persona1.get_edad()) 
print("________________________________")
persona1 = Estudiante("Nixson",18,"noveno")
print(persona1.get_nombre())
print(persona1.get_edad()) 
print(persona1.get_grado())         
print("________________________________")
estudiante = Estudiante("Nixson",18,"noveno")
print(estudiante.get_nombre())
print(estudiante.get_edad())
print(estudiante.get_grado())
print("________________________________")
persona1.set_nombre("Nixson")
persona1.set_edad(18)
persona1.set_grado("Noveno")
print(persona1.get_nombre())
print(persona1.get_edad()) 
print(persona1.get_grado())
print("________________________________")
estudiante = Estudiante("Pinacho","18 años",11)
print(f"El nombre del estudiante es {estudiante.get_nombre()} tiene {estudiante.get_edad()} y se encuentra en el curso de {estudiante.get_grado()}.")
estudiante.set_nombre("Nixson")
print("________________________________")
estudiante.set_edad(18)
estudiante.set_grado("Noveno")
print(f"El nombre del estudiante es {estudiante.get_nombre()} tiene {estudiante.get_edad()} y se encuentra en el curso de {estudiante.get_grado()}.")