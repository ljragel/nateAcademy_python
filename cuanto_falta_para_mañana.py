import datetime


manana=datetime.datetime.now()+ datetime.timedelta(days=1)
manana_medianoche=datetime.datetime(year=manana.year, month=manana.month, day=manana.day)

hoy=datetime.datetime.now()

lo_que_falta_para_manana=manana_medianoche-hoy


print("Lo que falta para manana es {}".format(lo_que_falta_para_manana))

print("Hoy es: {}".format(manana))