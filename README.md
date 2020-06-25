 # Búsquedas: Búsqueda de costo uniforme
   ##### Luis Ángel Delgado López, Nayeli Perea Rojas y Monica Durán Hernández
   
  ## **I. Introducción**
Este es un trabajo sobre la <u>_búsqueda de costo uniforme_</u>  , pero antes se dará una introducción de lo que son las **búsquedas**. 
Las técnicas de búsqueda son una serie de esquemas de representación del conocimiento, que mediante diversos algoritmos nos permite resolver problemas desde el punto de vista de la inteligencia artificial.

**Ejemplo de esquema:**


Es decir, son métodos en los que un agente puede seleccionar acciones en los ambientes deterministas, observables, estáticos y completamente conocidos, para poder encontrar la solución de un problema. En tales casos, el agente puede construir secuencias de acciones que alcanzan sus objetivos; a este proceso se le llama búsqueda.

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

Las búsquedas **no informadas** son aquellas que intentan encontrar la primera solución sin importar que tan óptima sea, no le importa la cantidad de pasos que pueda llevar.
Dentro de estás encontramos:

  * Exhaustiva
  * Aleatoria
  * Por profundidad
  * Por Amplitud
  * Costo Uniforme
  * Limitada por profundidad
  * Profundización iterativa 
  * Bidireccional.

Las búsquedas **heurísticas** son de un tipo inteligente ya que utiliza técnicas o mecanismos que se aproximan a la solución del problema de manera inteligente,es decir encuentran la solución en la menor cantidad de paso.
Dentro de estás encontramos:
* Búsqueda Tacaña 
* A* 
* Templado Simulado
* Búsqueda Tabú
* Búsqueda  Basada  en Restricciones.

A continuación nos dedicaremos a la búsqueda de costo uniforme.

 

## **II. Metodología**
La búsqueda de _costo uniforme (BCU)_ es un algoritmo de **búsqueda no informada** utilizado para recorrer sobre grafos el camino de costo mínimo entre un nodo raíz y un nodo destino, la búsqueda de costo uniforme expande el nodo **_n_** con el camino de costo más pequeño.

La búsqueda de _costo uniforme_ no se preocupa por el número de pasos que tiene un camino, pero si sobre su coste total. Por lo tanto, éste se meterá en un bucle infinito si expande un nodo que tiene una acción de coste cero que conduzca de nuevo al mismo estado.

Podemos garantizar  completitud si el costo de cada paso es mayor o igual a alguna constante positiva pequeña épsilon. Esta condición es también suficiente para asegurar optimización. Significa que el costo de un  camino siempre aumenta cuando vamos por él. De esta propiedad, es fácil ver que el algoritmo expande nodos que incrementan el coste del camino. Por lo tanto, el primer nodo objetivo seleccionado para la expansión es la solución óptima.

La búsqueda de _costo uniforme_ está dirigida por los costos de los caminos más que por las profundidades, entonces su complejidad no puede ser fácilmente caracterizada en términos de **_b_** y **_d_**  . En su lugar _**C***_ es el costo de la solución óptima, y se supone que cada acción cuesta al menos épsilon. Entonces la complejidad en tiempo y espacio del peor
caso del algoritmo es O(b<sup>[C*/épsilon]</sup>) la puede ser mucho mayor que **_b_<sup>_d_</sup>** Esto es porque la búsqueda de coste uniforme, y a menudo lo hace, explora los árboles grandes en pequeños pasos antes de explorar caminos que implican pasos grandes y quizá útiles. Cuando todos los costos son iguales, desde luego, la _b_<sup>[C*/épsilon]</sup> ) es justamente **_b_<sup>_d_</sup>** .
 


Demos un ejemplo de dicha búsqueda, para un mejor entendimiento, se pondrá un mapa.

**EJEMPLO:**
>Un turista desea viajar de Arad a Bucharest, pero desea viajar por carretera para conocer algunos lugares, pero desea tomar el recorrido con menos coste, para así poder comprar algunos recuerdos de las ciudades que posiblemente visitará.

El mapa siguiente, es un mapa de carreteras de parte de Rumanía.

![c](c.jpg)

Sabemos que el punto inicial es Arad, ahora vemos que Arad tiene tres vecinos Timisoara,  Zerind y Sibiu, el de coste menor entre los tres es a Zerind, luego de Zerind va a Oradea, de Oradea va a Sibiu, de Sibiu a Rimnicu Vilcea, de Rimnicu  Vilcea a Pitesti y de Pitesti a Bucharest el cual es el destino de nuestro turista, podemos ver el recorrido y el coste total en la siguiente imagen.

![9](https://user-images.githubusercontent.com/61295941/85773347-5b129f80-b6e3-11ea-9d46-824197c89758.jpg)

Como nos podemos dar cuenta, cuado estamos en Zerind, podemos tomar dos caminos los cuales son Arad y Oradea, vemos que toma el camino Zerind-Oradea ya que es el del menor coste, pero supongamos que el camino de Zerind-Arad fuera menor que Zerind-Oradea, no tomamos esa ruta ya que si la tomáramos nos  meteríamos en un ciclo infinito del cual no saldriamos, de igual forma podemos verlo para otros lugares, no contamos como vecino al lugar de dónde venimos (procedemos), para no meternos en un ciclo infinito.

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
**El código del anterior algoritmo es el siguiente:**

![IMG-20200618-WA0000](https://user-images.githubusercontent.com/61295941/85773349-5b129f80-b6e3-11ea-9f58-ef290aafe4b8.jpg)





## **III. Experimentos**
Para mostrar la ejecución del código se propone la tabla siguiente, que muestra el punto inicial y el punto destino.


| Recorridos deseados |
| :---------------------------------:|

| Punto inicial          | Destino               |
| :--------------------: | :-------------------: |
| Papantla (P)           | Boca del Rio (B)      |
| Papantla (P)           | Agua dulce (D)        |
| Agua dulce (D)         | San Andrés Tuxtla (S) |
| Xalapa (X)             | Alvarado (V)          |
| Huautla de Jimémez (E) | Minatitlan (M)        |
| Joachin (J)            | Xalapa (X)            |



**Tabla de las ciudades de veracruz**


![IMG-20200618-WA0007](https://user-images.githubusercontent.com/61295941/85773350-5bab3600-b6e3-11ea-82fa-6f7206919cdf.jpg)


**Mapa de Veracruz**

Para ir al mapa da click [aqui](https://luisangeld12.github.io/Busqueda2/)
 
El programa no muestra el costo total, pero en los siguientes recorridos se pondrá.

**Primer recorrido de P a B**


![IMG-20200625-WA0006](https://user-images.githubusercontent.com/61295941/85773360-5d74f980-b6e3-11ea-90ee-404b9032d58a.jpg)


Asi la ruta con menor costo que nos muestra el programa es:

| P     | T     | G     | Z     | B     |
| :---- | :---: | :---: | :---: | :---: |

Con un costo de: 248

El tiempo que tardo el programa en encontrar la ruta es: 0.000031 segundos

**Segundo recorrido de P a D**


![IMG-20200625-WA0004](https://user-images.githubusercontent.com/61295941/85773355-5c43cc80-b6e3-11ea-86ea-dd4dddae5f08.jpg)


Asi la ruta con menor costo que nos muestra el programa es:


| P     | T     | G     | Z     | B     | V     | S     | A     | M     | C     | D     |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

Con un costo de: 605

El tiempo que tardo el programa en encontrar la ruta es: 0.000038 segundos

**Tercer recorrido de D a S**

![IMG-20200625-WA0007](https://user-images.githubusercontent.com/61295941/85773342-59e17280-b6e3-11ea-91ea-5d1d65891fd0.jpg)

Asi la ruta con menor costo que nos muestra el programa es:



| D     | C     | M     | A     | S     |
| :---: | :---: | :---: | :---: | :---: |

Con un costo de: 212

El tiempo que tardo el programa en encontrar la ruta es: 0.000033 segundos

**Cuarto recorrido de X a V**


![IMG-20200625-WA0008](https://user-images.githubusercontent.com/61295941/85773345-5a7a0900-b6e3-11ea-8f3f-35ec9436baaa.jpg)


Asi la ruta con menor costo que nos muestra el programa es:



| X     | Z     | B     | V     |
| :---: | :---: | :---: | :---: |

Con un costo de: 174

El tiempo que tardo el programa en encontrar la ruta es: 0.000034 segundos

**Quinto recorrido de E a M**

![IMG-20200625-WA0003](https://user-images.githubusercontent.com/61295941/85773352-5bab3600-b6e3-11ea-885a-23535a88cbc0.jpg)



Asi la ruta con menor costo que nos muestra el programa es:



| E     | O     | J     | Y     | F     | H     | X     | Z     | B     | V     | S     | A     | M     |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

Con un costo de: 853

El tiempo que tardo el programa en encontrar la ruta es: 0.000057 segundos

**Sexto recorrido J a X**


![IMG-20200625-WA0005](https://user-images.githubusercontent.com/61295941/85773358-5cdc6300-b6e3-11ea-936b-491231306ca1.jpg)


Asi la ruta con menor costo que nos muestra el programa es:



| J     | Y     | F     | H     | X     |
| :---: | :---: | :---: | :---: | :---: |

Con un costo de: 232

El tiempo que tardo el programa en encontrar la ruta es: 0.000028 segundos

Cabe mencionar que las búsquedas anteriores se hicieron también manualmente, y se tardó 10 minutos con 53 segundos en encontrarlas, al igual que hubo confusiones en recorridos lejanos.



## **IV. Conclusiones**

Las búsquedas nos sirven para la solución de diferentes problemas, unas más óptimas que otras, además los programas les toma muy poco tiempo, como lo podemos notar en los experimentos. Encontrar rutas que a lo mejor a nosotros nos tomaria más tiempo,que incluso seria un poco tedioso ó fastidioso.


En la siguiente tabla se muestra la comparación del tiempo de ejecución que tarda cada programa en encontra la ruta de los siguientes tipos de búsqueda, dado el mismo punto inicial y mismo punto final.


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








