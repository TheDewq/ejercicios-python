palabra = input("ingresa un palabra: ")
palabra = palabra.upper()
palabra_no_vocales = "";
for x in palabra:
    if x == "A" or x == "E" or x == "I" or x == "O" or x = "U":
        continue
    palabra_no_vocales += x
print(palabra_no_vocales)
