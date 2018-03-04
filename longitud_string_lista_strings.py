
word_number=int(input("Introduce el numero de palabras de las cuales quieras saber la longitud"))
string_list=[]

aux=0

while aux<word_number:
    string_list.append(input("Introduce la palabra numero {}".format(aux+1)))
    aux += 1

long_string_list=[]

for str in string_list:
    long_string_list.append(str.__len__())

print(long_string_list)