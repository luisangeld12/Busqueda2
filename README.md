 # Búsquedas: Búsqueda de costo uniforme
   ##### Luis Ángel Delgado López, Nayeli Perea Rojas y Monica Durán Hernández
   
  ## **I. Introducción**
Este es un trabajo sobre la <u>_búsqueda de costo uniforme_</u>  , pero antes se dará una introducción de lo que son las **búsquedas**. 
Las búsqueda son una serie de esquemas que ayudan a la representación de diversos algoritmos, los cuales nos permite resolver problemas y dan una idea a lo que se refiere el algoritmo.

**Ejemplo de esquema:**

![ejemplo-de-b-squeda-de-coste-uniforme-l](https://user-images.githubusercontent.com/61295941/85778236-fd348680-b6e7-11ea-9069-d46650005f05.jpg)


Es decir, son métodos en los que un agente puede seleccionar acciones, para poder encontrar la solución de un problema. En tales casos, el agente puede construir secuencias de acciones que nos permiten alcanzar los objetivos; a este proceso se le llama búsqueda.

Los elementos que integran las búsqueda son:

* CONJUNTO DE ESTADO:
Todas las configuraciones posibles en el dominio.

* ESTADOS INICIALES:
Estados desde los que partimos, es decir nuestro punto inicial.

* ESTADOS FINALES:
Las soluciones del problema.

* OPERADORES:
Se aplica para pasar de un estado a otro.

* SOLUCIONADOR:
Mecanismo que nos permite evolucionar de un estado a otro mediante un algoritmo.

Dentro de las búsquedas podemos encontrar dos tipos, las **no informadas ó búsqueda a ciegas** y las **heurísticas**.

Las búsquedas **no informadas** son aquellas que intentan encontrar la primera solución sin importar que tan óptima sea, es decir; no le importa la cantidad de pasos que pueda llevar, nos puede dar una solución demaciado larga, cuando a lo mejor habia una solución mas corta y eficaz.

Dentro de estás encontramos:

  * Exhaustiva
  * Aleatoria
  * Por profundidad
  * Por Amplitud
  * Costo Uniforme
  * Limitada por profundidad
  * Profundización iterativa 
  * Bidireccional.

Las búsquedas **heurísticas** son de un tipo inteligente ya que utiliza técnicas o mecanismos que se aproximan a la solución del problema de manera eficiente,es decir encuentran la solución en la menor cantidad de paso.

Dentro de estás encontramos:
* Búsqueda Tacaña 
* A* 
* Templado Simulado
* Búsqueda Tabú
* Búsqueda  Basada  en Restricciones.


A continuación nos dedicaremos a la búsqueda de costo uniforme.

 

## **II. Metodología**

La búsqueda de _costo uniforme (BCU)_ es un algoritmo de **búsqueda no informada** utilizado para encontrar el camino de costo mínimo entre un punto inicial y un punto destino, la búsqueda de costo uniforme expande el nodo **_n_** (un punto inicial) con el camino de costo más pequeño.

La búsqueda de _costo uniforme_ no se preocupa por el número de pasos que tiene que tomar, pero si sobre su costo total. Por lo tanto, éste se meterá en un ciclo infinito si expande un nodo que tiene una acción de costo cero que conduzca de nuevo al mismo punto inicial.

Podemos garantizar  funcionalidad si el costo de cada paso es mayor o igual a alguna constante positiva pequeña, a la cual llamaremos  épsilon. Esta condición es suficiente para asegurar optimización. Significa que el costo de un  camino siempre aumenta cuando vamos por él, haciendo que el algoritmo expanda nodos que incrementan el costo del camino. Por lo tanto, el primer nodo objetivo (punto destino) seleccionado para la expansión es la solución más eficiente.

La búsqueda de _costo uniforme_ está dirigida por los costos de los caminos más que por las profundidades.


Demos un ejemplo de dicha búsqueda, para un mejor entendimiento, se pondrá un mapa.

**EJEMPLO:**

>Un turista desea viajar de Arad a Bucharest, pero desea viajar por carretera para conocer algunos lugares, pero desea tomar el recorrido con menos coste, para así poder comprar algunos recuerdos de las ciudades que posiblemente visitará.

El mapa siguiente, es un mapa de carreteras de parte de Rumanía.

![c](https://user-images.githubusercontent.com/61295941/85775756-b2197400-b6e5-11ea-8334-2d75c9b49f4e.jpg)

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

![code](https://github.com/luisangeld12/Busqueda2/blob/master/tests/code.png)





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


![tests1](https://github.com/luisangeld12/Busqueda2/blob/master/tests/tests1.png)


Asi la ruta con menor costo que nos muestra el programa es:

| P     | T     | G     | Z     | B     |
| :---- | :---: | :---: | :---: | :---: |

Con un costo de: 248

El tiempo que tardo el programa en encontrar la ruta es: 0.000039 segundos

**Segundo recorrido de P a D**


![test2](https://github.com/luisangeld12/Busqueda2/blob/master/tests/tests2.png)


Asi la ruta con menor costo que nos muestra el programa es:


| P     | T     | G     | Z     | B     | V     | S     | A     | M     | C     | D     |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

Con un costo de: 605

El tiempo que tardo el programa en encontrar la ruta es: 0.000047 segundos

**Tercer recorrido de D a S**

![tests3](https://github.com/luisangeld12/Busqueda2/blob/master/tests/tests3.png)


Asi la ruta con menor costo que nos muestra el programa es:



| D     | C     | M     | A     | S     |
| :---: | :---: | :---: | :---: | :---: |

Con un costo de: 212

El tiempo que tardo el programa en encontrar la ruta es: 0.000029 segundos

**Cuarto recorrido de X a V**


![tests4](https://github.com/luisangeld12/Busqueda2/blob/master/tests/tests4.png)


Asi la ruta con menor costo que nos muestra el programa es:



| X     | Z     | B     | V     |
| :---: | :---: | :---: | :---: |

Con un costo de: 174

El tiempo que tardo el programa en encontrar la ruta es: 0.000042 segundos

**Quinto recorrido de E a M**

![tests5](https://github.com/luisangeld12/Busqueda2/blob/master/tests/tests5.png)



Asi la ruta con menor costo que nos muestra el programa es:



| E     | O     | J     | Y     | F     | H     | X     | Z     | B     | V     | S     | A     | M     |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

Con un costo de: 853

El tiempo que tardo el programa en encontrar la ruta es: 0.000057segundos

**Sexto recorrido J a X**


![tests6](https://github.com/luisangeld12/Busqueda2/blob/master/tests/tests6.png)


Asi la ruta con menor costo que nos muestra el programa es:



| J     | Y     | F     | H     | X     |
| :---: | :---: | :---: | :---: | :---: |

Con un costo de: 232

El tiempo que tardo el programa en encontrar la ruta es: 0.000039 segundos

Cabe mencionar que las búsquedas anteriores se hicieron también manualmente, y se tardó 10 minutos con 53 segundos en encontrarlas, al igual que hubo confusiones en recorridos lejanos.



## **IV. Conclusiones**

Las búsquedas nos sirven para la solución de diferentes problemas, unas más óptimas que otras, además los programas les toma muy poco tiempo, como lo podemos notar en los experimentos. Encontrar rutas que a lo mejor a nosotros nos tomaria más tiempo,que incluso seria un poco tedioso ó fastidioso.


En la siguiente tabla se muestra la comparación del tiempo de ejecución que tarda cada programa en encontra la ruta de los siguientes tipos de búsqueda, dado el mismo punto inicial y mismo punto final.


| Comparación del tiempo de ejecución |
| :---------------------------------:|

| Tipo de búsqueda         | Inicio   | Destino    | Tiempo (seg) |
| :----------------------: | :------: | :--------: | :----------: |
| Búsquedas en amplitud    | Papantla | Agua Dulce | 0.000071     |
| Búsqueda  costo uniforme | Papantla | Agua Dulce | 0.000038     |
| Búsqueda en profundidad  | Papantla | Agua Dulce | 0.00009917   |
| A*                       | Papantla | Agua Dulce | 0.002065953  |
| Búsqueda Greedy          | Papantla | Agua Dulce | 0.0013936119 |

## **V. Bibliografía**

* [1] Stuart J. Russell y Peter Norvig. Inteligencia artificial, un enfoque moderno. _Segunda edición_ . Capítulos 3 y 4.

* [2] Video Clandestina: http://clandestina-hds.com/busquedasFinalProyect/busquedasFinalProyect.html 

* [3] Wikipedia: https://es.m.wikipedia.org/wiki/Búsqueda_de_costo_uniforme

* [4] Técnicas de búsquedas:https://sites.google.com/a/uniguajira.edu.co/inteligencia-artificial/tecnicas








