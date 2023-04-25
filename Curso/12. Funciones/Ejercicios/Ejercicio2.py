def factorial():
    from math import factorial
    factorialN = 1;
    n = int(input("Escribe un numero: "))
    if n < 0: 
        print("El numero no puede ser negativo")
    else:
        for i in range(1,n+1):
            factorialN *= i
        print("Factorial de {} es {}".format(n,factorialN))
        print("Factorial de {} es {}".format(n,factorial(n)))

factorial()