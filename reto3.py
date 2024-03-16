#reto 3

#realizar una funcion que revise si 2 palabras son anagramas, no aplica si son iguales

def determinar_anagrama(palabra1, palabra2):
    if palabra1 == palabra2:
        return False
    lst = list(palabra1)
    lst.sort()
    lst2 = list(palabra2)
    lst2.sort()
    if len(lst) != len(lst2):
        return False
    for i in range(len(lst)):
        if lst[i] != lst2[i]:
            return False
    return True

print(determinar_anagrama(input("ingrese una palabra: "), input("ingrese una palabra")))
