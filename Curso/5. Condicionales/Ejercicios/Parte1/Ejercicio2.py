numero = int(input("Escribe un numero: "))

if(numero >= 0):
    print("El valor absoluto de {} es {}".format(numero,numero))
else:
    print("El valor absoluto de {} es {}".format(numero,abs(numero)))