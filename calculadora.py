#muy facil, se puede despreciar
f_number=int(input("Introduce el primer numero con el que desees operar"))
operator= input("Introduce el operador de la operacion que desees realizar(MULTIPLICAR/SUMAR/RESTAR/DIVIDIR").upper()
second_number=int(input("Introduce el segundo numero de la operacion que quieres realizar"))


if f_number==""  or operator=="" or second_number=="" or  operator !="MULTIPLICACION" or operator!="DIVISION":
    print("Parametros no validos")



if operator=="SUMAR":
    print(f_number + second_number)

elif operator=="RESTAR":
    print(f_number - second_number)

elif operator=="MULTIPLICAR":
    print(f_number * second_number)

elif operator=="DIVIDIR":
    print(f_number/second_number)