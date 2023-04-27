'''
while True:
    try:
        numero = int(input("Ingresa un numero: "))
        resultado = 100 / numero
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es", edad)
        break
    except ValueError:
        print("Haz colocado un valor erroneo")

'''
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es", edad)
        break
    except KeyboardInterrupt:
        print("\nHaz cancelado la ejecucion")
        break