# Ejercicio modelar un Producto
# crear init con nombre, precio, stock
# vender() bajar stock solo si alcanza
# reponer() aumentar stock si cantidad > 0
# agregar mètodo valor_inventario() que devuelva precio x stock

class Producto():
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio 
        self.stock = stock
    
    def vender(self,cantidad):
        if cantidad <= self.stock:
            self.stock = self.stock - cantidad
            print(f"Vendiste {cantidad}, stock final = {self.stock}.")
        else:
            print("El stock disponible es menor de lo que se quiere vender")
        return self.stock
    
    def reponer(self,cantidad):
        if cantidad > 0:
            self.stock = self.stock + cantidad
            print(f"Repusiste {cantidad}. Stock final = {self.stock}")
        else:
            print("Debés ingresar una cantidad válida mayor a 0.")
        return self.stock
    
    def valor_inventario(self):
        valor_inventario = self.stock * self.precio
        return valor_inventario
        

chupetin = Producto("Evolution",10,20)
alfajor = Producto("Fulbito", 15, 5)

chupetin.vender(30)
chupetin.vender(5)
chupetin.reponer(-2)
chupetin.reponer(100)