# CarritoCompra
# crear 3 productos, agregarlos al carrito y mostrar el total a pagar
# bonus: evitar productos con precio menor o igual a cero
class Producto:
    def __init__(self,nombre,precio): # precio podria tener una property
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"El producto {self.nombre} cuesta $ {self.precio}"
    
class CarritoCompra:
    def __init__(self):
        self.productos = []
    
    # Evalua costo del producto mayor a 0 para agregarlo al carrito
    def agregar(self,producto):
        if producto.precio > 0:
            self.productos.append(producto)
        else:
            print(f"No es posible agregar el producto {producto.nombre} porque no tiene un precio válido")
    
    # Muestra precio final del carrito
    def total(self):
        precio_final = 0
        for producto in self.productos:
            precio_final = precio_final + producto.precio
        return f"El costo final del carrito es de $ {precio_final}"
    
    # Muestra productos del carrito
    def mostrar(self): 
        for producto in self.productos:
            print(producto)
# Creando productos    
shampoo = Producto("Sedal", 1000)
jabon = Producto("Dove",700)
detergente = Producto("Magistral",0)
aceite = Producto("Natura",2500)
# Creando carrito
compra_semanal = CarritoCompra()
# Agregando al carrito
compra_semanal.agregar(shampoo)
compra_semanal.agregar(jabon)
compra_semanal.agregar(detergente)
compra_semanal.agregar(aceite)
# Mostrar el detalle del carrito
compra_semanal.mostrar()
# Mostrar el precio final del carrito
print(compra_semanal.total())
