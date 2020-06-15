# Búsquedas: Búsqueda de costo uniforme
   ##### Luis Angel, Nayeli y Monica
  ## **I. Introducción**
Este es un trabajo sobre la _búsqueda de costo uniforme_ , pero antes se dara una intoducción de lo que son las **busquedas**. Las técnicas de búsqueda son una serie de esquemas de representación del conocimiento, que mediantes diversos algoritmos nos permite resolver problemas desde el punto de vista de la inteligencia artificial. Es decir,son métodos en los que un agente puede seleccionar acciones en los ambientes deterministas,observables,estaticos y completamente conocidos. En tales casos, el agente puede construir secuencias de acciones que alcanzan sus objetivos; a este proceso se le llama busqueda.
Los principales elementos que integran las técnicas de busqueda son:

* CONJUNTO DE ESTADO:
Todas las configuraciones posibles en el dominio.

* ESTADOS INICIALES:
Estados desde los que partimos.

* ESTADOS FINALES:
Las soluciones del problema.

* OPERADORES:
Se aplica para pasar de un estado a otro.

* SOLUCIONADOR:
Mecanismo que nos permite evolucionar de un estado a otro mediante un algoritmo.

Dentro de las búsquedas podemos encontrar dos tipos, las **no informadas ó búsqueda a ciegas** y las **heurísticas**.

Las búsquedas **no informadas** son aquellas que intentan encontrar la primera solución sin importar que tan optima sea.
Dentro de estás encontramos:

  * Exhaustiva
  * Aleatoria
  * por profundidad
  * por Amplitud
  * Costo Uniforme
  * Limitada por profundidad
  * Profundización iterativa y 
  * la Bidireccional.

Las busquedas **heuristicas** son de un tipo inteligente ya que utiliza técnicas o mecanismos que se aproximan a la solución del problema de manera inteligente.
Dentro de estás encontramos:


* Búsqueda Tacaña 

*A*
* Templado Simulado
* Búsqueda Tabú y 
* la Búsqueda  Basada  en Reestricciones.

A continuación nos dedicaremos a la búsque de costo uniforme.

## **II. Metodología**

La búsqueda de _costo uniforme (BCU)_ es un algoritmo de **búsqueda no informada** utilizado para recorrer sobre grafos el camino de costo mínimo entre un nodo raíz y un nodo destino, la búsqueda de costo uniforme expande el nodo _n_ con el camino de costo más pequeño. 

La búsqueda de costo uniforme no se preocupa por el número de pasos que tiene un camino, pero si sobre su coste total. Por lo tanto, éste se meterá en un bucle infinito si expande un nodo que que tiene una acción de coste cero que conduzca de nuevo al mismo estado.
Podemos garantizar  completitud si el costo de cada paso es mayor o igual a alguna constante positiva pequeña épsilon. Esta condición es también suficiente para asegurar optimización. Significa que el costo de un  camino siempre aumenta cuando vamos por él. De esta propiedad, es fácil ver que el algoritmo expande nodos que incrementan el coste del camino. Por lo tanto, el primer nodo objetivo seleccionado para la expansión es la solución óptima.


![ejemplo](https://image.slideserve.com/618935/ejemplo-de-b-squeda-de-coste-uniforme-l.jpg)



Para mostrar como funciona la busqueda de costo  uniforme se dara un pequeño problema.
Una familia de Arad desea tomar unas vacaciones y  desean vistar  Pitesti, a continuacion se muestra un mapa


![ejemplo](http://www.cs.us.es/~fsancho/images/2015-07/c685bc9e-178f-11e2-bb76-001e670c2818.jpg)

y desean saber que camino tomar para que el coste no sea tanto.


El algoritmo de esta búsqueda es el siguiente: 

## **III. Experimentos**

Para mostrar la ejecusión de programa se dara un ejemplo o la solución de un problem , la siguiente tabla muetsra nuestros  recorridos que seseamos hacer



| Punto inicial | Destino |
| :-----------: | :-----: |
| b1            |         |
| b2            |         |
| b3            |         |
| b4            |         |



## **IV. Conclusiones**

Las búsquedas nos sirven para la solución de diferentes problemas unas mas optimas que otras,en la siguiente tabla se muestra la comparación del tiempo de ejecución de las siguientes tipos de búsqueda.


| Comparación del tiempo de ejecución |
| :---------------------------------:|

| Tipo de búsqueda         | Inicio | Destino | Tiempo |
| :----------------------: | :----: | :-----: | :----: |
| Búsquedas en amplitud    |        |         |        |
| Búsqueda  costo uniforme |        |         |        |
| Búsqueda en pronfundidad |        |         |        |
| A*                       |        |         |        |
| Búsqueda Greedy          |        |         |        |


## **V. Bibliografía**


[1]

[2]

[3]

[4]






