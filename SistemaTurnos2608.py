# Sistema simple de turnos
# bonus: no permitir dos turnos con la misma fecha y hora
# Sistema simple de turnos
# bonus: no permitir dos turnos con la misma fecha y hora
class Paciente:
    def __init__(self,nombre,dni):
        self.nombre = nombre
        self.dni = dni
    def __str__(self):
        return f"Paciente {self.nombre} - DNI: {self.dni}"
    
class Turno:
    def __init__(self,paciente,fecha,hora):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
    
    def __str__(self):
        return f"Día {self.fecha} Hora {self.hora} Paciente {self.paciente}"
    
class Agenda:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self,turno):
        for t in self.turnos: #recorriendo la lista de turnos
            if t.paciente == turno.paciente:
                if t.fecha == turno.fecha and t.hora == turno.hora:
                    return f"Ya hay un turno el día {turno.fecha} a las {turno.hora}" # si ya esta en lista mismo dia y hora, muestra el return y termina la funcion
        self.turnos.append(turno) # si no está, no ingresa al if por lo que una vez terminado el for, agrega el turno en el listado
        return f"El turno del {turno.fecha} a las {turno.hora} fue ingresado con éxito."
    
    def listar_turnos(self):
        print("---Turnos confirmados (Agenda)---")
        for t in self.turnos:
            print(t)

paciente1 = Paciente("Aguila Aguilar","34452")
paciente2 = Paciente("Aguar Alar","22345")
turno_dermo = Turno(paciente1,"27-05","14hs")
turno_clinico = Turno(paciente1,"25-07","14hs")
turno_neuro = Turno(paciente2,"27-05","14hs")
turno_labo = Turno(paciente1,"2-09","15hs")
turno_pediatra = Turno(paciente2,"27-05","14hs")
agenda_rossi = Agenda()
print(agenda_rossi.agregar_turno(turno_dermo))
print(agenda_rossi.agregar_turno(turno_clinico))
print(agenda_rossi.agregar_turno(turno_neuro))
print(agenda_rossi.agregar_turno(turno_labo))
print(agenda_rossi.agregar_turno(turno_pediatra))
print(agenda_rossi.listar_turnos())
