#Crear una clase estudiante que tenga los atributos nombre, edad y grado.

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
niño1=Estudiante("Crisiano",",18",",once")
niño2=Estudiante("Messi",",16",",decimo")
niño3=Estudiante("Garnacho",",12",",quinto")
print(niño1.nombre, niño1.grado)
print(niño2.edad)
print(niño3.grado)