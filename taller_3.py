class Estudiante:
    def __init__(self, nombre, edad, grado, nota1, nota2):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.nota1 = nota1
        self.nota2 = nota2
    def saludar(self):
        print(f"Hola mucho gusto {self.nombre} que tiene {self.edad} y esta en {self.grado}.")
    def suma_notas(self):
        suma = self.nota1 + self.nota2
        promedio = suma / 2
        print(f"La suma de las notas es {suma}.")
        print(f"Y el promedio es {promedio}")
nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
grado = input("Digite su grado: ")
nota1 = int(input("Digite la primera nota: "))
nota2 = int(input("Digite la segunda nota: "))
estudiante1 = Estudiante(nombre, edad, grado, nota1, nota2)
estudiante2 = Estudiante("Nixson", 33, "once", 40, 30)
estudiante1.saludar()
estudiante1.suma_notas()
estudiante2.saludar()
estudiante2.suma_notas()
