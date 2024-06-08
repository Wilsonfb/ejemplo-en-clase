class Precio:
    def __init__(self, precio, garantia):
        self.precio = precio
        self.garantia =  garantia 
    def descricion(self):
        print(f"Precio: {self.precio} y garantia {self.garantia}.")
class Tipo:
    def __init__(self, tipo):
        self.tipo = tipo
    def descricion(self):   
        print(f"Tipo: {self.tipo}.")
class Cilla:
    def __init__(self, material, tipo, precio):
        self.material = material 
        self.tipo = tipo
        self.precio = precio
    def descricion(self):
        print(f"Material: {self.material}.")
        self.tipo.descricion()
        self.precio.descricion()
precio = Precio(10000, "1 año")
tipo = Tipo("Gamer")
cilla = Cilla("Plastico", tipo, precio)
cilla.descricion()