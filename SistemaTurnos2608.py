# Sistema simple de turnos
# bonus: no permitir dos turnos con la misma fecha y hora
class Paciente:
    def __init__(self,nombre,dni):
        self.nombre = nombre
        self.dni = dni
    def __str__(self):
        return f"Paciente: {self.nombre} DNI: {self.dni}"
    
class Turno:
    def __init__(self,paciente,fecha,hora):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
    def __str__(self):
        return f"Turno para {self.paciente} el día {self.fecha} a las {self.hora}"
    
class Agenda:
    def __init__(self):
        self.turnos = []
    def agregar_turno(self,turno):
        for t in self.turnos:
            if t.fecha == turno.fecha and t.hora == turno.hora:
                print("Ya tiene un turno asignado para ese día y horario.")
                return # corta la función si ya tiene un turno igual
        self.turnos.append(turno)
        print(f"El turno del {turno.fecha} a las {turno.hora} quedó confirmado.")
        
            
    def listar_turnos(self):
        print("• Lista de turnos confirmados:")
        for turno in self.turnos:
            print(turno)
            
    
paciente1 = Paciente("Pepe diaz",123456)
agenda1 = Agenda()

turno1 = Turno(paciente1,"22-05","15hs")
agenda1.agregar_turno(turno1)

turno2 = Turno(paciente1,"22-06","14hs")
agenda1.agregar_turno(turno2)

turno3 = Turno(paciente1,"22-05","15hs")
agenda1.agregar_turno(turno3)

turno4 = Turno(paciente1,"22-05","14hs")
agenda1.agregar_turno(turno4)

agenda1.listar_turnos()