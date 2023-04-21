lista = []
nuevaLista = []

def perdirNumeros():
    terminar = 0
    while terminar == 0:
        numero = int(input("Ingresa un numero, Escribe 0 para salir: "))
        if numero == 0:
            print("Lista desordenada: {}".format(lista))
            listaOrdenada()
            terminar = 1
        else: 
            lista.append(numero)
            nuevaLista.append(numero)

def listaOrdenada():
    print("Lista ordenada: {}".format(nuevaLista.sort()))


perdirNumeros()