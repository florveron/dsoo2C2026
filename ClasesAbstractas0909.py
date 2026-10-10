# Clases abstractas
# Crear personaje como clase abs y tres clases concretas
from abc import ABC, abstractmethod

class Personaje(ABC):
    @abstractmethod
    def atacar(self):
        pass
        
class Guerrero(Personaje):
    def atacar(self):
        return f"Ataco con espada"
    
class Mago(Personaje):
    def atacar(self):
        return f"Ataco con fuego"

class Arquero(Personaje):
    def atacar(self):
        return f"Ataco con flecha" 
gue = Guerrero()
mag = Mago()
arq = Arquero()

personajes = [gue.atacar(),
mag.atacar(),
arq.atacar()]
for p in personajes:
    print(p)

