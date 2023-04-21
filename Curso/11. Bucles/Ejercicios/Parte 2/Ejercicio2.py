numero1 = int(input("Escribe el primero numero: "))
numero2 = int(input("Escribe el segundo numero: "))

for i in range(numero1,numero2+1):
    if i%2 == 0:
        continue
    print(i)