palabra1 = input("Escribe una palabra: ")
palabra2 = input("Escribe otra palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No riman porque tienen menos de 3 caracteres")
elif(palabra1[-3:] == palabra2[-3:]):
    print("Las palabras riman")
elif (palabra1[-2:] == palabra2[-2:]):
    print("Las palabras riman un poco")
else:
    print("Las palabras NO riman")
