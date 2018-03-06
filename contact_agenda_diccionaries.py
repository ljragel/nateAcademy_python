
agenda=dict()
stop=False


while stop==False:
    print("¿Quieres añadir un nuevo contacto a al agenda? (Yes/No).")
    answ=input("Respuesta: ")

    if answ=="No":
        stop=True
    elif answ=="Yes":
        contact_name=input("Introduce el nombre del contacto: ")
        contact_tlf=input("Introduce el teléfono de tu contacto")

        agenda[contact_name]=contact_tlf
        stop=True

print("Estos son los contactos de tu agenda")
print(agenda)