tupla = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z")

seleccion = int(input("Escribe un numero y te dire que letra corresponde en el alfabeto: "))

if seleccion > len(tupla):
    print("El numero no puede ser mayor a {}".format(len(tupla)))
elif seleccion <= 0:
    print("El numero no puede ser menor a 0")
else: 
    print("El numero {} corresponde a la letra {}".format(seleccion,tupla[seleccion-1]))