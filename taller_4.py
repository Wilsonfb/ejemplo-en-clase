#Crear una clase llamada rectangulo con los parametros de base y altura con un objeto que sea calcular_area.
class Rectngulo:
    def __init__ (self,base,altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        print(f"El area del rectangulo es: {self.altura * self.base}.")
altura = float(input("Digite la altura: "))
base = float(input("Digite la base: "))
rectangulo1 = Rectngulo(altura, base)
rectangulo1.calcular_area()
