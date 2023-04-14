diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Escribe el nombre de un pais: ")
pais = pais.title()
if pais in diccionario.keys():
    print("La capital de {} es {}".format(pais,diccionario.get(pais)))
else:
    print("El pais no se encuentra")