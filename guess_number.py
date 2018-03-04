
secret_number=73
my_number=0
accountant=0

while secret_number != my_number:
    accountant+=1
    my_number=int(input("Introduce el numero que crees que es, este es tu intento numero: {}".format(int(accountant))))

print("ENHORABUENA! Has adivinado el numero que estaba pensando, lo has hecho en {} intentos".format(accountant))
print("Porque el 73 es el mejor numero, porque es el vigesimo primer numero primo, su espejo, el 37 es el decimo segundo, y su espejo ,el 21 es el producto multiplicar 7 por 3")