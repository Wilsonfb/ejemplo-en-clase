class Motor:
    def __init__(self, tipo, cilindros):
        self.tipo = tipo
        self.cilindros = cilindros
    def describir(self):
        print(f"Motor: {self.tipo}, {self.cilindros} cilindros.")
class Llanta: 
    def __init__(self, material, uso ):
        self.material = material
        self.uso = uso
    def describir(self):
        print(f"Llantas: {self.material} y uso {self.uso}.")
class Coche:
    def __init__(self, marca, modelo, motor, llanta):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.llanta = llanta
    def describir(self):
        print(f"Coche: {self.marca} y modelo {self.modelo}.")
        self.motor.describir()
        self.llanta.describir()
motor_coche = Motor("Gasolina", 4)
llanta = Llanta("Caucho", "costante")
mi_coche = Coche("Toyota", "Corolla", motor_coche, llanta)
mi_coche.describir()