'''
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final
'''

valorP1 = float(input("Calificación práctica 1: "))
valorP2 = float(input("Calificación práctica 2: "))
valorP3 = float(input("Calificación práctica 3: "))
valorEP = float(input("Calificación examen parcial: "))
valorEF = float(input("Calificación examen final: "))

promedio = (((valorP1 + valorP2 + valorP3) / 3) + (2*valorEP) + (3*valorEF))/6

print("La calificacion final es:",promedio)