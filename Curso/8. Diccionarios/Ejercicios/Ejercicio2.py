diccionario = {
    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"
}

seleccion = int(input("Ingresa un numero y te doy un jugador: "))

if seleccion in diccionario.keys():
    print("El jugador con la playera {} es {}".format(seleccion,diccionario.get(seleccion)))
else:
    print("No tengo ningun jugador para ti")