
from time import sleep

import datetime

NIGHT_STARTS=20
DAY_STARTS=7

def main():
    current_time=datetime.datetime.now()
    while True:
        sleep(0.7)

        current_time+= datetime.timedelta(hours=1)

        if current_time.hour> NIGHT_STARTS or current_time.hour< DAY_STARTS:
            day_night_label="Noche"
        else:
            day_night_label="Dia"
        with open("horas.txt", "a") as  hours_file:
            # esto abre el archivo que le pasamos en el primer parametro en el modo que le pasamos por el segundo parametro
            hours_file.write("La hora actual es {}, es de {}\n".format(current_time, day_night_label))
            print("La hora actual es {}, es de {}".format(current_time, day_night_label))


if __name__=="__main__":
    main()
