 # Búsquedas: Búsqueda de costo uniforme
   ##### Luis Ángel Delgado López, Nayeli Perea Rojas y Monica Durán Hernández
   
  ## **I. Introducción**
  
Este es un trabajo sobre la _búsqueda de costo uniforme_  , pero antes se dará una introducción de lo que son las **búsquedas**. Las técnicas de búsqueda son una serie de esquemas de representación del conocimiento, que mediantes diversos algoritmos nos permite resolver problemas desde el punto de vista de la inteligencia artificial. Es decir, son métodos en los que un agente puede seleccionar acciones en los ambientes deterministas, observables, estáticos y completamente conocidos. En tales casos, el agente puede construir secuencias de acciones que alcanzan sus objetivos; a este proceso se le llama búsqueda.
Los principales elementos que integran las técnicas de búsqueda son:

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
  * Por profundidad
  * Por Amplitud
  * Costo Uniforme
  * Limitada por profundidad
  * Profundización iterativa y 
  * La Bidireccional.

Las búsquedas **heurísticas** son de un tipo inteligente ya que utiliza técnicas o mecanismos que se aproximan a la solución del problema de manera inteligente.
Dentro de estás encontramos:
* Búsqueda Tacaña 
* A* 
* Templado Simulado
* Búsqueda Tabú y 
* La Búsqueda  Basada  en Restricciones.

A continuación nos dedicaremos a la búsqueda de costo uniforme.

 

## **II. Metodología**
La búsqueda de _costo uniforme (BCU)_  es un algoritmo de **búsqueda no informada** utilizado para recorrer sobre grafos el camino de costo mínimo entre un nodo raíz y un nodo destino, la búsqueda de costo uniforme expande el nodo **_n_** con el camino de costo más pequeño.

La búsqueda de costo uniforme no se preocupa por el número de pasos que tiene un camino, pero si sobre su coste total. Por lo tanto, éste se meterá en un bucle infinito si expande un nodo que tiene una acción de coste cero que conduzca de nuevo al mismo estado.
Podemos garantizar  completitud si el costo de cada paso es mayor o igual a alguna constante positiva pequeña épsilon. Esta condición es también suficiente para asegurar optimización. Significa que el costo de un  camino siempre aumenta cuando vamos por él. De esta propiedad, es fácil ver que el algoritmo expande nodos que incrementan el coste del camino. Por lo tanto, el primer nodo objetivo seleccionado para la expansión es la solución óptima.

La búsqueda de _costo uniforme_ está dirigida por los costos de los caminos más que por las profundidades, entonces su complejidad no puede ser fácilmente caracterizada en términos de **_b_** y **_d_**  . En su lugar _**C***_ es el costo de la solución óptima, y se supone que cada acción cuesta al menos épsilon. Entonces la complejidad en tiempo y espacio del peor
caso del algoritmo es O(b<sup>[C*/épsilon]</sup> ) la puede ser mucho mayor que _b_<sup>_d_</sup> Esto es porque la búsqueda de coste uniforme, y a menudo lo hace, explora los árboles grandes en pequeños pasos antes de explorar caminos que implican pasos grandes y quizá útiles. Cuando todos los costos son iguales, desde luego, la _b_<sup>[C*/épsilon]</sup> ) es justamente _b_<sup>_d_</sup> .
 


Demos un ejemplo de dicha búsqueda, para un mejor entendimiento, se pondrá un mapa.
**EJEMPLO:**
>Un turista desea viajar de Arad a Bucharest, pero desea viajar por carretera para conocer algunos lugares, pero desea tomar el recorrido con menos coste para así poder comprar algunos recuerdos de las ciudades que posiblemente visitará.

El mapa siguiente, es un mapa de carreteras simplificado de parte de Rumanía.
![c](c.jpg)
Sabemos que el punto inicial es Arad, ahora vemos que Arad tiene tres vecinos Timisoara,  Zerind y Sibiu, el de coste menor entre los tres es a Zerind, luego de Zerind va a Oradea, de Oradea va a Sibiu,de Sibiu a Rimnicu Vilcea, de Rimnicu  Vilcea a Pitesti y de Pitesti a Bucharest el cual es el destino de nuestro turista, podemos ver el recorrido y el coste total en la 
siguiente imagen.

![1](1.jpg)

Como nos podemos dar cuenta, cuado estamos en Zerind, podemos tomar dos caminos los cuales son Arad y Oradea, vemos que toma el camino Zerind-Oradea ya que es el del menor coste, pero supongamos que el camino de Zerind-Arad fuera menor que Zerind-Oradea, no tomamos esa ruta ya que si la tomáramos nos  meteríamos en un ciclo infinito del cual no saldriamos, de igual forma podemos verlo para otros lugares, no contamos como vecino al lugar de donde venimos (procedemos), para no meternos en un ciclo infinito.

Podemos definir el algoritmo de _Búsqueda De Costo Uniforme_ como se presenta a continuación.

```
Costo(mapa,inicio,destino)-> lista
      arbol(inicio)
      recorrido(inicio,None)
      MIENTRAS noVacio(arbol) HACER
           ciudad <- sacar.arbol()
           SI ciudad es destino ENTONCES
                 RETORNAR ruta
           FIN-SI
           PARACADA vecinoOrdenadoDeCiudad HACER:
               SI vecino no existe  en recorrido ENTONCES
                    agrega.arbol(vecino)
                    agrega.recorrido(vecino,ciudad)
                    SALIDA-FORZADA
               FIN-SI
           FIN-PARA
      FIN-MIENTRAS
FIN-COSTO
               
           
```
El código del anterior algoritmo es el siguiente:



## **III. Experimentos**
Para mostrar la ejecución del código se propone la tabla siguiente, que muestra el punto inicial y el punto destino.


| Recorridos deseados |
| :---------------------------------:|

| Punto inicial | Destino           |
| :-----------: | :---------------: |
| Papantla      | Boca del Rio      |
| Coatza        | Otatitlán         |
| Agua dulce    | San Andrés Tuxtla |
| Joachin       | Xalapa            |
| Xalapa        | Alvarado          |
| Zempoala      | Fortin            |




## **IV. Conclusiones**

Las búsquedas nos sirven para la solución de diferentes problemas, unas más óptimas que otras.


En la siguiente tabla se muestra la comparación del tiempo de ejecución de los siguientes tipos de búsqueda, dado el mismo punto inicial y final.


| Comparación del tiempo de ejecución |
| :---------------------------------:|

| Tipo de búsqueda         | Inicio | Destino  | Tiempo |
| :----------------------: | :----: | :------: | :----: |
| Búsquedas en amplitud    | Xalapa | Alvarado |        |
| Búsqueda  costo uniforme | Xalapa | Alvarado |        |
| Búsqueda en profundidad  | Xalapa | Alvarado |        |
| A*                       | Xalapa | Alvarado |        |
| Búsqueda Greedy          | Xalapa | Alvarado |        |

## **V. Bibliografía**

* [1] Stuart J. Russell y Peter Norvig. Inteligencia artificial, un enfoque moderno. _Segunda edición_ . Capítulos 3 y 4.

* [2] Video Clandestina: http://clandestina-hds.com/busquedasFinalProyect/busquedasFinalProyect.html 

* [3] Wikipedia: https://es.m.wikipedia.org/wiki/Búsqueda_de_costo_uniforme

* [4] Técnicas de búsquedas:https://sites.google.com/a/uniguajira.edu.co/inteligencia-artificial/tecnicas



