while True:
    try:
        edad = int(input("Edad: "))
        print("Tu edad es",edad)
        break
    except:
        print("Valor invalido")
    finally:
        print("La ejecucion ha finalizado")