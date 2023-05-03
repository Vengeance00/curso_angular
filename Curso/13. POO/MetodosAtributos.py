class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensaje):
        return mensaje
    
    def escucharMusica(self):
        print("Estas escuchando musica")

celular = FabricaTelefonos()
#print(celular.marca)
celular.marca = "Apple"
#print(celular.marca)

#print(celular.llamar("Hola, ¿Con quien hablo?"))
celular.escucharMusica()