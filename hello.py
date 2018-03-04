number_to_guess=2

user_number=int(input("introduce el numero que crees que es"))


if number_to_guess== user_number:
    print("Lo has adivinado")
else:
    user_number = int(input("introduce el numero que crees que es, segundo intento"))
    if number_to_guess== user_number:
        print("Lo has adivinado")
    else:
        user_number = int(input("introduce el numero que crees que es, tercer intento"))
        if number_to_guess == user_number:
            print("Lo has adivinado")
        else:
            user_number = int(input("introduce el numero que crees que es, cuarto intento"))
            if number_to_guess == user_number:
                print("Lo has adivinado")
            else:
                user_number = int(input("introduce el numero que crees que es, quinto intento"))
                if number_to_guess == user_number:
                    print("Lo has adivinado")
                else:
                    print("lo sentimos, has perdido")
print("EJERCICIO DE PROGRAMACION MUY FACIL, ESTRUCTURA DE CONTROL IF ELSE")



