lista = []

def perdirNumeros():
    terminar = 0
    while terminar == 0:
        numero = int(input("Ingresa un numero, Escribe 0 para salir: "))
        if numero == 0:
            print("Lista: {}".format(lista))
            listaOrdenada()
            terminar = 1
        else: 
            lista.append(numero)

def listaOrdenada():
    lista.sort()
    pares = []
    inpares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else: 
            inpares.append(i)
    print("Pares: {}".format(pares))
    print("Inpares: {}".format(inpares))

perdirNumeros()