class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0
    
    def implementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador
    
a = A()
# print(a.cuenta)
# a.cuenta = 30
# print(a.cuenta)