class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    '''
    def numLlantas(self):
        print("El vehiculo tiene {} llantas".format(self.llantas))
    
    def colorVehiculo(self):
        print("El vehiculo es de color {}".format(self.color))
    
    def precioVehiculo(self):
        print("El precio del vehiculo es ${}".format(self.precio))
    '''

class Moto(Fabrica):
    '''
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)
    '''
    def datos(self):
        print("La moto tiene {} llantas".format(self.llantas))
        print("La moto es de color {}".format(self.color))
        print("El precio de la moto es ${}".format(self.precio))

class Carro(Fabrica):
    '''
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)
    '''
    def datos(self):
        print("El carro tiene {} llantas".format(self.llantas))
        print("El carro es de color {}".format(self.color))
        print("El precio del carro es ${}".format(self.precio))

moto = Moto(2,"Rojo",23999)
moto.datos()
#moto.numLlantas()
#moto.colorVehiculo()
#moto.precioVehiculo()

carro = Carro(4,"Negro",239500)
carro.datos()
#carro.numLlantas()
#carro.colorVehiculo()
#carro.precioVehiculo()