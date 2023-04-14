votacion = input("Elige un candidato (ABC): ")

if votacion.upper() == "A":
    print("Usted ha votado por el partido ROJO")
elif votacion.upper() == "B":
    print("Usted ha votado por el partido VERDE")
elif votacion.upper() == "C":
    print("Usted ha votado por el partido AZUL")
else:
    print("Opcion errónea")