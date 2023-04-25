def entero():
    print("Este es un valor entero: ")
    return 10

def decimal():
    print("Este es un valor decimal: ")
    return 90.99

def frase():
    return "Mi nombre es juan"

def asignacion():
    return 1,2,3,4,5

print(entero())
print(decimal())
print(frase())

a,b,c,d,e = asignacion()
print(a)