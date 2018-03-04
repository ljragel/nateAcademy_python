
frase_usuario=input("Introduce la frase que te salga de las narices: ")
vocales=["a", "e", "i", "o", "u"]
vocales_mayusculas=["A", "E", "I", "O", "U"]
vocales_en_el_texto=[]

numero_mayusculas=0
numero_vocales=0
numero_consonantes=0
numero_espacios=0
numero_comas=0
numero_puntos=0

for letra in frase_usuario:
    if (letra in vocales):
        numero_vocales+=1
        vocales_en_el_texto.append(letra)
    elif (letra in vocales_mayusculas):
        numero_mayusculas+=1
        vocales_en_el_texto.append(letra)
    elif letra==" ":
        numero_espacios+=1
    elif letra==",":
        numero_comas+=1
    elif letra==".":
        numero_puntos+=1
    elif letra==letra:
        numero_consonantes+=1
    elif letra==letra.upper():
        numero_mayusculas+=1
        numero_consonantes+=1

print("Vocales: ")
print(vocales_en_el_texto)

print("")
print("")

print("El numero de vocales es {}".format(numero_vocales))
print("El numero de consonantes es {}".format(numero_consonantes))
print("El numero de puntos es {}".format(numero_puntos))
print("El numero de comas es {}".format(numero_comas))
print("El numero de espacios es {}".format(numero_espacios))
print("El numero de mayusculas es {}".format(numero_mayusculas))



