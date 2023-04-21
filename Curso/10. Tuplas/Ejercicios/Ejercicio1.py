tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

seleccion = int(input("Escribe un numero y te dare el mes al que pertenece: "))

if seleccion > len(tupla):
    print("El numero no puede ser mayor a {}".format(len(tupla)))
elif seleccion <= 0:
    print("El numero no puede ser menor de 1")
else:
    print("El mes {} es {}".format(seleccion,tupla[seleccion-1]))
