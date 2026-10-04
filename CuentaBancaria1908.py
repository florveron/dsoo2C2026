# Ejercicio CuentaBancaria
# Reglas
# saldo empieza en 0
# no permitir saldo negativo

class CuentaBancaria():
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0 # no se incluye como parámetro para respetar la regla de siempre comenzar en 0
        
    def depositar(self,monto):
        if monto > 0:
            self.saldo = self.saldo + monto
        else:
            print("Depositá un importe mayor a 0")
        return self.saldo
    
    def extraer(self,monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo = self.saldo - monto
            else:
                print("Extraé un monto menor")
        else:
            print("Ingresá un número mayor a 0.")
        return self.saldo
    
cuenta_ahorro = CuentaBancaria("Pipo Lopez")
print(cuenta_ahorro.saldo)
cuenta_ahorro.depositar(10)
print(cuenta_ahorro.saldo)
cuenta_ahorro.extraer(-100)
print(cuenta_ahorro.saldo)
cuenta_ahorro.extraer(9)
print(cuenta_ahorro.saldo)




