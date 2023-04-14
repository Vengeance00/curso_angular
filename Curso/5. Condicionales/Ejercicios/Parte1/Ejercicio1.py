vocal = input("Escribe una vocal: ")

# if vocal.lower() == 'a' or vocal.lower() == 'e' or vocal.lower() == 'i' or vocal.lower() == 'o' or vocal.lower() == 'u':
#     print("Es vocal")
# else:
#     print("No es vocal")

if vocal.lower() in "aeiou":
    print("Es vocal")
else:
    print("No es vocal")