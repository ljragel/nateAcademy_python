import datetime

AVERAGE_LIFESPAN=80 #que este en mayusculas significa que es una constante
SMOKER_PENALIZATION=10
SEDENTARISM_PENALIZATION=5
DRINKER_PENALIZATION=10

#esta funcion crea una linea de separacion entre el texto que se imprimem y el siguiente
def print_with_underscores(message):
    print(message)
    print(len(message) * "-")

def ask_yes_or_not(message):
    response=None

    while response != "S" and response != "N":
        response = input(message.upper()+ " [S/N]")

    return response=="S"

print("¡Completa esta encuesta para saber cuanto tiempo de vida te queda!")

birth_date=input("Introduce tu fecha de nacimiento con el siguiente formato: dd/mm/yy")
datetime.datetime.now()

#esto parsea la fecha, es decir, le decimos como debe de interpretar lo que nos pasan
#en resumen, le estoy diciendo a python, en que posicion estan los numeros que necesita
birth_date=datetime.datetime.strptime(birth_date, "%d/%m/%Y")
years_lost=0


if ask_yes_or_not("¿Fumas?"):
    years_lost+= SMOKER_PENALIZATION

if ask_yes_or_not("¿Bebes?"):
    years_lost+= DRINKER_PENALIZATION

if not ask_yes_or_not("¿Haces deporte frecuentemente?"):
    years_lost+= SEDENTARISM_PENALIZATION

lifespan= AVERAGE_LIFESPAN- years_lost
death_day= birth_date + datetime.timedelta(days=lifespan*365)

days_to_death= death_day- datetime.datetime.now()

print("Fecha de la muerte {}, te queda {}".format(death_day.strftime("%d/%m/%Y"), days_to_death))
