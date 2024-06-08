class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial=0.0):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        return False
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        return False
    def consultar_saldo(self):
        return self.__saldo
    def obtener_numero_cuenta(self):
        return self.__numero_cuenta
class Cliente:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__cuentas = []
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def agregar_cuenta(self, cuenta_bancaria):
        if isinstance(cuenta_bancaria, CuentaBancaria):
            self.__cuentas.append(cuenta_bancaria)
            return True
        return False
    def eliminar_cuenta(self, numero_cuenta):
        for cuenta in self.__cuentas:
            if cuenta.obtener_numero_cuenta() == numero_cuenta:
                self.__cuentas.remove(cuenta)
                return True
        return False
    def consultar_saldo_total(self):
        saldo_total = sum(cuenta.consultar_saldo() for cuenta in self.__cuentas)
        return saldo_total
cuenta1 = CuentaBancaria("123456789", 1000)
cuenta2 = CuentaBancaria("987654321", 2000)
cliente = Cliente("Juan Pérez")
cliente.agregar_cuenta(cuenta1)
cliente.agregar_cuenta(cuenta2)
print(f"Saldo total de {cliente.get_nombre()} {cliente.consultar_saldo_total()}.")
cuenta1.depositar(500)
print(f"Saldo total de {cliente.get_nombre()} después de depositar en la cuenta 1: {cliente.consultar_saldo_total()}.")
cuenta2.retirar(1000)
print(f"Saldo total de {cliente.get_nombre()} de retirar de la cuenta 2: {cliente.consultar_saldo_total()}.")
cliente.eliminar_cuenta("123456789")
print(f"Saldo total de {cliente.get_nombre()} después de eliminar la cuenta 1: {cliente.consultar_saldo_total()}.")
