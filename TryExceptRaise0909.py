#-------------- EJERCICIO 1
# Crear pedir_edad(): debe pedir una edad hasta que sea válida.
def validar_edad(mensajito):
    while True:
        try:
            edad = int(input(mensajito))
            if edad > 0:
                return edad
            else:
                print("ingresá un nro mayor a 0")
        except ValueError :
            print("No ingresaste un nro")
            
def pedir_edad():
    a = validar_edad("Ingresa un nroo:")
    return a

print(pedir_edad())

#-------------- EJERCICIO 2
# Crear dividir_seguro(a, b): si b es 0, mostrar error.

def dividir_seguro(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir por 0.")
    
dividir_seguro(10,0)

#-------------- EJERCICIO 3
# Crear retirar(saldo, monto): validar monto positivo y saldo suficiente.

def retirar(saldo,monto):
    try:
        if monto > 0:
            if monto <= saldo:
                saldo = saldo - monto
                return saldo
            else:
                return "Debés retirar un monto menor."
        else: 
            return "Ingresá un monto mayor a 0"
    except TypeError:
        return "Ingresá un valor numérico"
    
print(retirar(100,20))
print(retirar(10,"a"))
print(retirar(50,100))
print(retirar("b",10))

#-------------- EJERCICIO 4
# Crear una excepción propia llamada ProductoSinStockError.

class ProductoSinStockError(Exception):
    pass

#-------------- EJERCICIO 5
# Leer números hasta escribir salir y manejar valores inválidos.

def validar_numero():
    while True:
        a = (input("Ingresa un valor:"))
        if a.lower() == "salir":
            return "El programa finalizó."
        try:
            num = int(a)
            print(f"Ingresaste {a}")
        except ValueError:
            print("ingresaste un valor inválido") # si uso un return, el bucle while no continúa, el programa se corta

print(validar_numero())