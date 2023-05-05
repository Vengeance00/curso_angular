class Calculadora():
    def __init__(self):
        #self._numero1 = numero1
        #self._numero2 = numero2
        self._numero1 = int(input("Escribe un numero: "))
        self.numero2 = int(input("Escribe otro numero: "))
    
    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1(self,numero1):
        self._numero1 = numero1
    
    @property
    def numero2(self):
        return self._numero2
    
    @numero2.setter
    def numero2(self, numero2):
        self._numero2 = numero2
    
    def suma(self):
        print(self._numero1 + self._numero2)

    def resta(self):
        print(self._numero1 - self._numero2)

    def multiplicacion(self):
        print(self._numero1 * self._numero2)

    def division(self):
        print(self._numero1 / self._numero2)

#numero1 = int(input("Escribe un numero: "))
#numero2 = int(input("Escribe otro numero: "))

#calculadora = Calculadora(numero1,numero2)
calculadora = Calculadora()
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.division()