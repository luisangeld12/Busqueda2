from modules import search as sc

print('Ingrese la letra correspondiente a la ciudad de inicio ')
n = str(input())

search_cost = sc.busqueda(sc.map_city, 'F', 'B')
print(search_cost)
