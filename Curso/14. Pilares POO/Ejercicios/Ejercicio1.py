class Estudiante():
    def __init__(self,nombre,nota):
        self._nombre = nombre
        self._nota = nota

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, nota):
        self._nota = nota

    def imprimir(self):
        print("Nombre: {}\nNota: {}".format(self.nombre,self.nota))

    def mensaje(self):
        if self._nota >= 6:
            print("Aprobado")
        else:
            print("Reprobado")


estudiante = Estudiante("Juan",6)
estudiante.imprimir()
estudiante.mensaje()

estudiante = Estudiante("Pedro",5)
estudiante.imprimir()
estudiante.mensaje()