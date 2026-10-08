# ------EJERCICIO 1
# Crear clase Producto con nombre, precio, property para validar precio positivo

class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio # llama inmediatamente al @precio.setter. al crear el obj y pasar el atributo, si o si pasara por la validacion
        
    @property
    def precio(self):
        return self._precio # es necesario usar self._precio para guardar/leer el valor real en memoria de forma segura
    
    @precio.setter
    def precio(self,p):
        if p > 0:
            self._precio = p # es necesario usar self._precio para guardar/leer el valor real en memoria de forma segura
        else:
            raise ValueError("El precio debe ser mayor a cero") 
jabon = Producto("Dove",10)
jabon.precio = 6
print(jabon.precio)
jabon.precio = 26
print(jabon.precio)
try:    #estamos capturando el error para probar q la validacion funciona sin que se detenga el programa
    jabon.precio = -6
except ValueError as e:
    print(e) #imprime el precio debe ser mayor a cero
print(jabon.precio) # imprime el ultimo valor valido prtegido

# ------EJERCICIO 2
# Crear clase Cuenta con depositar, retirar y property saldo solo lectura.
class Cuenta:
    def __init__(self,nombre,saldo):
        self.nombre = nombre
        self._saldo = saldo
        
    def depositar(self,monto):
        if monto > 0:
            self._saldo = self._saldo + monto
            return self._saldo
        else:
            raise ValueError("Ingresa un nro mayor a 0")
    def retirar(self,monto):
        if monto > 0 :
            if monto <= self._saldo:
                self._saldo = self._saldo - monto
                return self._saldo
            else:
                raise ValueError("Ingresa un nro menor")
        else:
            raise ValueError("Ingresa un nro mayor a 0")
    @property
    def saldo(self):
        return self._saldo

# ------EJERCICIO 3
# Crear clase Empleado y subclases Programador y Diseñador, cada una implementa trabajar().

class Empleado():
    def trabajar(self):
        print("estoy trabajando")
        
class Programador(Empleado):
     def trabajar(self):
            print("estoy trabajando en el código")
            
class Diseñador(Empleado):
         def trabajar(self):
            print("estoy trabajando en el diseño")
            
empleados= [Empleado(),Programador(),Diseñador()]
for e in empleados:
    e.trabajar()
    
# ------EJERCICIO 4   
# Crear clase Rectangulo con property area y perimetro.

class Rectangulo:
    def __init__(self,lado_a,lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    @property
    def area(self):
        return self.lado_a * self.lado_b
    
    @property
    def perimetro(self):
        return (self.lado_a*2) + (self.lado_b*2)
    
rojo = Rectangulo(3,4)
print(rojo.area)
print(rojo.perimetro)
rojo.lado_a = 5
print(rojo.area)
print(rojo.perimetro)

# ------EJERCICIO 5
# Modelar Auto con composición: Auto tiene Motor. El método arrancar() usa el motor.
class Motor:
    def arrancar(self):
        return "Rrum Rrum"
    
class Auto:
    def __init__(self):
        self.motor = Motor() # El auto se crea y contiene su propio motor interno
        
    def arrancar(self):
        return self.motor.arrancar() # el obj auto le delega la accion de arrancar al motor

mi_auto = Auto()
print(mi_auto.arrancar())