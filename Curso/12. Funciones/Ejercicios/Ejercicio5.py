def areaCuadrado(base,altura):
    return base * altura

def areaCirculo(radio):
    from math import pi
    return pi * (pow(radio,2));

print(areaCuadrado(10,5))
print(areaCirculo(10))