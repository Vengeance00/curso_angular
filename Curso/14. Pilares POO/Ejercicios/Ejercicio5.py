class Universidad():
    def __init__(self):
        self.nombreUniversidad = ""

class Carrera():
    def __init__(self):
        self.especialidad = ""
    
class Estudiante():
    def __init__(self):
        self.nombre = ""
        self.edad = 0

class Persona(Universidad,Carrera,Estudiante):
    def __init__(self, universidad, especialidad, nombre, edad):
        self.nombreUniversidad = universidad
        self.especialidad = especialidad
        self.nombre = nombre
        self.edad = edad
    
    def datos(self):
        print("El alumno se llama {}".format(self.nombre))
        print("La edad de {} es {} años".format(self.nombre,self.edad))
        print("{} estudia en {} la especialidad en {}".format(self.nombre,self.nombreUniversidad,self.especialidad))


persona = Persona("UTP","TICS","Juan",26)
persona.datos()
