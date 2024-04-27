#Crear una clase llamada rectangulo con los parametros de base y altura con un objeto que sea calcular_area.
class Rectngulo:
    def _init_(self,base,altura):
        self.base=base
        self.altura=altura
    def calcular_area(self):
        print(f"El area del rectangulo es: {altura*base}")
altura=float(input("Digite la altura: "))
base=float(input("Digite la base: "))
rectangulo1=Rectngulo()
rectangulo1.calcular_area()