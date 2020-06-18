from modules import search as sc
import time

print('Ingrese la letra correspondiente a la ciudad de inicio ')
start = str(input())
print('Ingrese la letra correspondiente a la ciudad de llegada ')
end = str(input())

start_time = time.time()
search_cost = sc.busqueda(sc.map_city, start, end)
end_time = time.time()
all_time = round(end_time - start_time, 1000)

print('\nLa ruta de la búsqueda de costo uniforme es: ', search_cost)
print('El tiempo que tardó en realizar la búsqueda es : ', all_time)
