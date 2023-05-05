class Marino():
    def hablar(self):
        print("Hola...")

class Pulpo(Marino):
    def hablar(self):
        print("Soy un Pulpo")

class Foca(Marino):
    '''
    def __init__(self, mensaje):
        self._mensaje = mensaje
    @property
    def mensaje(self):
        return self._mensaje
    
    @mensaje.setter
    def mensaje(self, mensaje):
        self._mensaje = mensaje
    
    def mostrarMensaje(self):
        print("El mensaje es {}".format(self._mensaje))
    '''
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(self.mensaje)

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Soy una foca")
