
numero_de_numeros=float(input("Dime cuantos numeros quieres multiplicar, no introduzcas el 0 ya que se anulara el resultado."))
number_list=[]

aux=0

while aux<numero_de_numeros:
    number_list.append(float(input("Introduce tu numero, numero {}".format(aux+1))))
    aux+=1

multiplication_result=1

for number in number_list:
     if number!=0:
        multiplication_result= multiplication_result* number

print(multiplication_result)