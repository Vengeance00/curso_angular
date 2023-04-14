vocal = input("Escribe una vocal en minuscula: ")

letra = input("Escribe una letra en mayuscula: ");

lista_vocales = ["a","e","i","o","u"]

if vocal != vocal.lower():
    print("La vocal no es una minuscula")
else:
    if vocal in lista_vocales:
        if letra != letra.upper():
            print("La letra no es una mayuscula")
        else:
            letra = letra.lower()
            vocal = vocal.upper()
            print("La vocal en mayuscula: {}\nLa letra en minuscula: {}".format(vocal,letra));
    else:
        print("La vocal es incorrecta")

