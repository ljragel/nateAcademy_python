import datetime

t0= datetime.datetime.now()

#esto es para ralentizar el programa asi que se ignora
for i in range(0, 100000000):
    suma= i


tf=datetime.datetime.now()

delta= tf-t0

print("El tiempo de ejecución del for han sido: {}".format(delta.total_seconds())+ " segundos.")