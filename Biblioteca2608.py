# Biblioteca mínima
# primero, crear dos libros y agregarlos a la biblioteca

class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
        
    def __str__(self):
        return f"{self.titulo} de {self.autor}"    
    def prestar():
        pass
    def devolver():
        pass
    
class Biblioteca:
    def __init__(self,nombre):
        self.nombre = nombre
        self.libros = []
        
    def agregar_libro(self,libro):
        self.libros.append(libro)

    def buscar_por_titulo():
        pass
    
    def mostrar_disponibles(self):
        for libro in self.libros:
            print(libro)
            

libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")
libro2 = Libro ("El resplandor", "Stephen King")
biblioteca_local = Biblioteca("Local")
biblioteca_local.agregar_libro(libro1)
biblioteca_local.agregar_libro(libro2)
biblioteca_local.mostrar_disponibles()