from typing import List
import heapq

tree = []
travel = []


def busqueda(mapa, start, end) -> List[float]:
    heapq.heappush(tree, start)
    while len(tree) != 0:
        city = heapq.heappop(tree)
        if start == end:
            return end
        for vecino in mapa[city]:
            if vecino not in travel:
                heapq.heappush(tree, vecino)
                travel.append(vecino)


# Usando la tabla de ciudades proporcionada por la mtra paty :)
map_city = {
    'A': [(95, 'S'), (52, 'M'), (100, 'N')],
    'B': [(114, 'X'), (61, 'V'), (62, 'J'), (49, 'Z')],
    'C': [(43, 'D'), (22, 'M'), (169, 'S')],
    'D': [(43, 'C')],
    'E': [(208, 'F'), (138, 'O')],
    'F': [(43, 'H'), (25, 'Y'), (208, 'E')],
    'G': [(116, 'Z'), (180, 'X'), (75, 'P'), (40, 'T')],
    'H': [(43, 'F'), (120, 'X')],
    'J': [(62, 'B'), (44, 'Y'), (78, 'O')],
    'M': [(22, 'C'), (52, 'A')],
    'N': [(95, 'O'), (180, 'A')],
    'O': [(95, 'N'), (78, 'J'), (120, 'V'), (138, 'E')],
    'P': [(75, 'G'), (43, 'T'), (119, 'U')],
    'S': [(95, 'A'), (84, 'V'), (169, 'C')],
    'T': [(43, 'P'), (40, 'G')],
    'U': [(104, 'X'), (119, 'P')],
    'V': [(84, 'S'), (61, 'B'), (120, 'O')],
    'X': [(104, 'U'), (64, 'Z'), (114, 'B'), (120, 'H'), (180, 'G')],
    'Y': [(25, 'F'), (44, 'J')],
    'Z': [(64, 'X'), (49, 'B'), (116, 'G')]
}
