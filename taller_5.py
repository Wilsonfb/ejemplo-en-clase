class Cirulo:
    def __init__(self,radio):
        self.radio = radio
    def calcular_perimetro(self):
        radio_del_circulo = 2 * 3.14 * self.radio
        print(f"El perimetro es {radio_del_circulo}.")
radio = float(input("Digite el radio: "))
circulo1 = Cirulo(radio)
circulo1.calcular_perimetro()