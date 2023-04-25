def factorial():
    factorial = 1;
    n = int(input("Escribe un numero: "))
    for i in range(1,n+1):
        factorial *= i
    print("Factorial de {} es {}".format(n,factorial))

factorial()