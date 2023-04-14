import math

valorA = float(input("Escribe el valor de a: "))
valorB = float(input("Escribe el valor de b: "))
valorC = float(input("Escribe el valor de c: "))
x1 = 0
x2 = 0
if (valorB**2 - (4*valorA*valorC)) < 0:
    print("No se puede ejecutar porque no se puede sacar raiz a un numero negativo")
else:
    x1 = (-valorB + math.sqrt((valorB**2)-(4*valorA*valorC))) / (2*valorA)
    x2 = (-valorB - math.sqrt((valorB**2)-(4*valorA*valorC))) / (2*valorA)
    print("La solucion es: \nx1=",x1,"\nx2=",x2)
# solucion1 = (-valorB + math.sqrt(valorB**2 - (4*valorA*valorC))) / (2*valorA)
# solucion2 = (-valorB - math.sqrt(valorB**2 - (4*valorA*valorC))) / (2*valorA)
# print("La solucion es:",solucion1)