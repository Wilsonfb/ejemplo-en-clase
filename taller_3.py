class Estudiante:
    def init(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def saludar(self):
        print(f"Su nombre es {self.nombre} tiene {self.edad} años y esta en {self.grado}.")
    def suma(valor1, valor2):
        valor1 = 10
        valor2 = 20
        suma = valor1 + valor2
        print(f"La suma es {suma}.")
#nombre = input("Digite su nombre: ")
#edad = input("Digite su edad: ")
#grado = input("Digite su grado: ")
#obejto1 = Estudiante(nombre, edad, grado)
obejto1 = Estudiante(nombre= "nixson", edad =18, grado=11)
#print(f"Su nombre {obejto1.nombre} esta en {obejto1.grado} y tiene {obejto1.edad} años.")
obejto1.saludar()
obejto1.suma()