from typing import List
import heapq

tree = []
travel = []


def busqueda(mapa, start: str, end: str) -> List[str]:
    heapq.heappush(tree, start)
    travel.append(start)
    while len(tree) != 0:
        city = heapq.heappop(tree)
        if city == end:
            return travel
        for neighbor in mapa[city]:
            if neighbor[1] not in travel:
                heapq.heappush(tree, neighbor[1])
                travel.append(neighbor[1])
                break


# Usando la tabla de ciudades proporcionada por la mtra paty :)
map_city = {
    'A': [(52, 'M'), (95, 'S'), (180, 'N')],
    'B': [(49, 'Z'), (61, 'V'), (62, 'J'), (114, 'X')],
    'C': [(22, 'M'), (43, 'D'), (169, 'S')],
    'D': [(43, 'C')],
    'E': [(138, 'O'), (208, 'F')],
    'F': [(25, 'Y'), (43, 'H'), (208, 'E')],
    'G': [(40, 'T'), (75, 'P'), (116, 'Z'), (180, 'X')],
    'H': [(43, 'F'), (120, 'X')],
    'J': [(44, 'Y'), (62, 'B'), (78, 'O')],
    'M': [(22, 'C'), (52, 'A')],
    'N': [(95, 'O'), (180, 'A')],
    'O': [(78, 'J'), (95, 'N'), (120, 'V'), (138, 'E')],
    'P': [(43, 'T'), (75, 'G'), (119, 'U')],
    'S': [(84, 'V'), (95, 'A'), (169, 'C')],
    'T': [(40, 'G'), (43, 'P')],
    'U': [(104, 'X'), (119, 'P')],
    'V': [(61, 'B'), (84, 'S'), (120, 'O')],
    'X': [(64, 'Z'), (104, 'U'), (114, 'B'), (120, 'H'), (180, 'G')],
    'Y': [(25, 'F'), (44, 'J')],
    'Z': [(49, 'B'), (64, 'X'), (116, 'G')]
}
