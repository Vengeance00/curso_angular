def numeros():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    if n1 > n2:
        return 1
    elif n2 > n1:
        return -1
    else:
        return 0

print(numeros())