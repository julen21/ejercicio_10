import stats_data as s_d

lista = []
while True:
    número = input("números para estadísticas: ")
    if número == "fin":
        break
    número = float(número)
    lista.append(número)
calculo_stats = s_d.StatsData(lista)

print("Lista números: ",calculo_stats.l_data)
print("Media: ",calculo_stats.mean)
print("Mediana: ",calculo_stats.median)
print("Varianza: ",calculo_stats.variance)
