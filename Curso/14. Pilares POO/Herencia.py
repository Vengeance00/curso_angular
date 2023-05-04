class Animales():
    def hablar(self):
        print("Yo soy un animal")

    def descripcion(self):
        print("Yo soy un {}".format(self.animal))

class Perro(Animales):
    pass

class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal

perro = Perro()
perro.hablar()

abeja = Abeja("abeja");
abeja.descripcion()