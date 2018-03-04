
mi_lista=[]
input_usuario= input("Que quieres comprar. Escribe fin para para salir")

while input_usuario!= "FIN":
    mi_lista.append(input_usuario)
    input_usuario=input("Que necesitas comprar. Escribe fin para salir.")

largo_lista=mi_lista.__len__()
indice_actual=0

while indice_actual<largo_lista:
    print("Tengo que comprar  {}  ".format(mi_lista[indice_actual]) + "HECHO CON WHILE")
    indice_actual+=1

print("Esta es tu lista de la compra")

#con while es una cosa muy cutre salchichera, ahora lo vamos a hacer con un for

for item in mi_lista:
    print("Tengo que comprar  {}  ".format(item) + "HECHO CON UN FOREACH DE PYTHON, QUE ES CASI MAGIA")