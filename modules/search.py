import heapq

#Hice una cola de prioridad por cada ciudad, erroneamente use los nombres, los actualizaré con las letras del abecedario para mejor uso

Acayucan = []
heapq.heappush(Acayucan, (95, 'San Andrés Tuxtla'))
heapq.heappush(Acayucan, (52, 'Minatitlán'))
heapq.heappush(Acayucan, (180, 'Nigromante'))
print('Acayucan: ', Acayucan)
m_costo2 = heapq.heappop(Acayucan)
print('El menor costo saliendo de Acayucan es hacia: ', m_costo2)

Boca = []
heapq.heappush(Boca, (114, 'Xalapa'))
heapq.heappush(Boca, (61, 'Alvarado'))
heapq.heappush(Boca, (62, 'Joachin'))
heapq.heappush(Boca, (49, 'Zempoala'))
print('\nBoca del Rio: ', Boca)
m_costo3 = heapq.heappop(Boca)
print('El menor costo saliendo de Boca del Rio es hacia: ', m_costo3)

Coatzacoalcos = []
heapq.heappush(Coatzacoalcos, (43, 'Agua Dulce'))
heapq.heappush(Coatzacoalcos, (22, 'Minatitlán'))
heapq.heappush(Coatzacoalcos, (169, 'San Ándres Tuxtla'))
print('\nCoatzacoalcos: ', Coatzacoalcos)
m_costo4 = heapq.heappop(Coatzacoalcos)
print('El menor costo saliendo de Coatzacoalcos es hacia: ', m_costo4)

Agua = []
heapq.heappush(Agua, (43, 'Coatzacoalcos'))
print('\nAgua dulce: ', Agua)
m_costo5 = heapq.heappop(Agua)
print('El menor costo saliendo de Agua Dulce es hacia: ', m_costo5)

Huautla = []
heapq.heappush(Huautla, (208, 'Fortín de las flores'))
heapq.heappush(Huautla, (138, 'Otatitlán'))
print('\nHuautla de Jiménez: ', Huautla)
m_costo6 = heapq.heappop(Huautla)
print('El menor costo saliendo de Huautla de Jiménez es hacia: ', m_costo6)

Fortin = []
heapq.heappush(Fortin, (43, 'Huatusco'))
heapq.heappush(Fortin, (25, 'Yanga'))
heapq.heappush(Fortin, (208, 'Huautla de Jimenéz'))
print('\nFortín de las flores: ', Fortin)
m_costo7 = heapq.heappop(Fortin)
print('El menor costo saliendo de Fortín de las flores es hacia: ', m_costo7)

Vega = []
heapq.heappush(Vega, (116, 'Zempoala'))
heapq.heappush(Vega, (180, 'Xalapa'))
heapq.heappush(Vega, (75, 'Papantla'))
heapq.heappush(Vega, (40, 'Tecolutla'))
print('\nVega de Alatorre: ', Vega)
m_costo8 = heapq.heappop(Vega)
print('El menor costo saliendo de Vega de Alatorre es hacia: ', m_costo8)

Huatusco = []
heapq.heappush(Huatusco, (43, 'Fortín de las flores'))
heapq.heappush(Huatusco, (120, 'Xalapa'))
print('\nHuatusco: ', Huatusco)
m_costo9 = heapq.heappop(Huatusco)
print('El menor costo saliendo de Huatusco es hacia: ', m_costo9)

Joachin = []
heapq.heappush(Joachin, (62, 'Boca del Río'))
heapq.heappush(Joachin, (44, 'Yanga'))
heapq.heappush(Joachin, (78, 'Otatitlán'))
print('\nJoachin: ', Joachin)
m_costo10 = heapq.heappop(Joachin)
print('El menor costo saliendo de Joachin es hacia: ', m_costo10)

Minatitlan = []
heapq.heappush(Minatitlan, (22, 'Coatzacoalcos'))
heapq.heappush(Minatitlan, (52, 'Acayucan'))
print('\nMinatitlán: ', Minatitlan)
m_costo11 = heapq.heappop(Minatitlan)
print('El menor costo saliendo de Minatitlán es hacia: ', m_costo11)

Nigromante = []
heapq.heappush(Nigromante, (95, 'Otatitlán'))
heapq.heappush(Nigromante, (180, 'Acayucan'))
print('\nEl Nigromante: ', Nigromante)
m_costo12 = heapq.heappop(Nigromante)
print('El menor costo saliendo de El Nigromante es hacia: ', m_costo12)

Otatitlan = []
heapq.heappush(Otatitlan, (95, 'Nigromante'))
heapq.heappush(Otatitlan, (78, 'Joachin'))
heapq.heappush(Otatitlan, (120, 'Alvarado'))
heapq.heappush(Otatitlan, (138, 'Huautla'))
print('\nOtatitlán: ', Otatitlan)
m_costo13 = heapq.heappop(Otatitlan)
print('El menor costo saliendo de Otatitlán es hacia: ', m_costo13)

Papantla = []
heapq.heappush(Papantla, (75, 'Vega de Alatorre'))
heapq.heappush(Papantla, (43, 'Tecolutla'))
heapq.heappush(Papantla, (119, 'Teziutlán'))
print('\nPapantla: ', Papantla)
m_costo1 = heapq.heappop(Papantla)
print('El menor costo saliendo de Papantla es hacia: ', m_costo1)

Tuxtla = []
heapq.heappush(Tuxtla, (95, 'Acayucan'))
heapq.heappush(Tuxtla, (84, 'Alvarado'))
heapq.heappush(Tuxtla, (169, 'Coatzacoalcos'))
print('\nSan Ándres Tuxtla: ', Tuxtla)
m_costo14 = heapq.heappop(Tuxtla)
print('El menor costo saliendo de San Ándres Tuxtla es hacia: ', m_costo14)

Tecolutla = []
heapq.heappush(Tecolutla, (43, 'Papantla'))
heapq.heappush(Tecolutla, (40, 'Vega de Alatorre'))
print('\nTecolutla: ', Tecolutla)
m_costo15 = heapq.heappop(Tecolutla)
print('El menor costo saliendo de Tecolutla es hacia: ', m_costo15)

Teziutlan = []
heapq.heappush(Teziutlan, (104, 'Xalapa'))
heapq.heappush(Teziutlan, (119, 'Papantla'))
print('\nTeziutlán: ', Teziutlan)
m_costo16 = heapq.heappop(Teziutlan)
print('El menor costo saliendo de Teziutlán es hacia: ', m_costo16)

Alvarado = []
heapq.heappush(Alvarado, (84, 'San Ándres Tuxtla'))
heapq.heappush(Alvarado, (61, 'Boca del Rio'))
heapq.heappush(Alvarado, (120, 'Otatitlán'))
print('\nAlvarado: ', Alvarado)
m_costo17 = heapq.heappop(Alvarado)
print('El menor costo saliendo de Alvarado es hacia: ', m_costo17)

Xalapa = []
heapq.heappush(Xalapa, (104, 'Teziutlán'))
heapq.heappush(Xalapa, (64, 'Zempoala'))
heapq.heappush(Xalapa, (114, 'Boca del Rio'))
heapq.heappush(Xalapa, (120, 'Huatusco'))
heapq.heappush(Xalapa, (180, 'Vega de Alatorre'))
print('\nXalapa: ', Xalapa)
m_costo18 = heapq.heappop(Xalapa)
print('El menor costo saliendo de Xalapa es hacia: ', m_costo18)

Yanga = []
heapq.heappush(Yanga, (25, 'Fortín de las flores'))
heapq.heappush(Yanga, (44, 'Joachin'))
print('\nYanga: ', Yanga)
m_costo19 = heapq.heappop(Yanga)
print('El menor costo saliendo de Yanga es hacia: ', m_costo19)

Zempoala = []
heapq.heappush(Zempoala, (64, 'Xalapa'))
heapq.heappush(Zempoala, (49, 'Boca del Rio'))
heapq.heappush(Zempoala, (116, 'Vega de Alatorre'))
print('\nZempoala: ', Zempoala)
m_costo20 = heapq.heappop(Zempoala)
print('El menor costo saliendo de Zempoala es hacia: ', m_costo20)

