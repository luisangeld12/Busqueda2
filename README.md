# INTRODUCIÓN

Este es un trabajo sobre la búsqueda de costo uniforme,pero antes se daran una intoducción de lo que son las busquedas.\\Las técnicas de busqueda son una serie de esquemas de representación del conocimiento,que mediantes diversos algoritmos nos permite resolver problemas desde el punto de vista de la inteligencia artificial.
Es decir,son métodos en los que un agente puede seleccionar acciones en los ambientes deterministas,observables,estaticos y completamente conocidos.En tales casos, el agente puede construir secuencias de acciones que alcanzan sus objetivos; a este proceso se le llama busqueda.
Los principales elementos que integran las técnicas de busqueda son:

CONJUNTO DE ESTADO:
Todas las configuraciones posibles en el dominio.

ESTADOS INICIALES:
Estados desde los que partimos.

ESTADOS FINALES:
Las soluciones del problema.

OPERADORES:
Se aplica para pasar de un estado a otro.

SOLUCIONADOR:
Mecanismo que nos permite evolucionar de un estado a otro mediante un algoritmo.

Dentro de las busquedas podemos encontrar dos tipos, las no informadas ó búsqueda a ciegas y las heuristicas.
Las busquedas no informadas son aquellas que intentan encontrar la primera solución sin importar que tan optima sea.
Dentro de estás encontramos:Exhaustiva,Aleatoria,por profundidad,por Amplitud,Costo Uniforme,Limitada por profundidad,Profundización iterativa y la Bidireccional.
Las busquedas heuristicas son de un tipo inteligente ya que utiliza técnicas o mecanismos que se aproximan a la solución del problema de manera inteligente.
Dentro de estás encontramos:Busqueda Tacaña, A ,Templado Simulado, Búsqueda Tabú y la Búsqueda  Basada  en Reestricciones.
A continuación nos dedicaremos a la búsque de costo uniforme.

# METODOLOGÍA

La búsqueda de costo uniforme (BCU) es un algoritmo de búsqueda no informada utilizado para recorrer sobre grafos el camino de costo mínimo entre un nodo raíz y un nodo destino, la búsqueda de costo uniforme expande el nodo n con el camino de costo más pequeño.\\
La búsqueda de costo uniforme no se preocupa por el número de pasos que tiene un camino,pero si sobre su coste total. Por lo tanto, éste se meterá en un bucle infinito si expande un nodo que que tiene una acción
de coste cero que conduzca de nuevo al mismo estado.
Podemos garantizar  completitud si el costo de cada paso es mayor o igual a alguna constante positiva pequeña \epsilon .Esta condición es también suficiente para asegurar optimización.Significa que el costo de un  camino siempre aumenta cuando vamos por él.De esta propiedad, es facil ver que el algoritmo expande nodos que incrementan el coste del camino.Por lo tanto,el primer nodo objetivo seleccionado para la expansión es la solución óptima.
La búsqueda de costo uniforme está dirigida por los costo de los caminos más que por las profundidades, entonces su complejidad no puede ser fácilmente caracterizada en téeminos de b y d. En su lugar (aqui va una formula) es el coste de la solución óptima, y se supone que cada acción cuesta al menos \epsilon. Entonces la complejidad en tiempo y espacio del peor caso del algoritmo es (aqui va una formula), la cual puede ser mucho mayor que (aqui va otra formula). Esto es porque la búsqueda de coste uniforme, y a menudo lo hace, explora los árboles grandes en pequeños pasos antes de explorar caminos que implican pasos grandes y quizá útiles. Cuando todos los costos son iguales, desde luego, la (aqui va otra formula) es justamente (aqui va otra formula).


