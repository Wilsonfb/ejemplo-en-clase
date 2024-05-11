class calculadora:
    def __init__ (self):
        self.resultado = None
    def sumar(self):
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        self.resultado = num1 + num2 
        print(f"El resultado de la suma es {self.resultado}.")
    def multiplicar(self):
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        self.resultado = num1* num2
        print(f"El resultado de la multiplicacion es {self.resultado}.")
    def dividir(self):
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        self.resultado = num1 / num2 
        print(f"El resultado de la divicion es: {self.resultado}.")
    def promedio(self):
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        self.resultado = num1 + num2 
        self.resultado = self.resultado / 2
        print(f"El resultado del promedio es {self.resultado}.")
while True:
    operacion = calculadora()
    num = int(input('''
                    ¿Que operacion quiere hacer?
                    1-Suma.  
                    2-Multiplicacion.  
                    3-Divicion.  
                    4-Promedio.
                    5-Salir.
                    Digita que quieres hacer: '''))
    if num == 1:
        print("Suma")
        operacion.sumar()
    elif num == 2:
        print("Multiplicacion")
        operacion.multiplicar()
    elif num == 3:
        print("Divicion")
        operacion.dividir()
    elif num == 4: 
        print("Promedio")
        operacion.promedio()
    elif num == 5:
        break
    else:
        print("Digita un numero pre definido porfa.")