# final_proyect_sockets

implementa tres algoritmos de ordenamiento: mergesort, heapsort y quicksort.

Mergesort es un algoritmo de ordenamiento recursivo que divide el arreglo en dos mitades, ordena cada mitad y luego combina las dos mitades ordenadas en un solo arreglo ordenado.

Heapsort es un algoritmo de ordenamiento que utiliza un heap binario para ordenar los elementos. Primero se construye un heap a partir del arreglo y luego se extraen los elementos del heap en orden ascendente.

Quicksort es un algoritmo de ordenamiento recursivo que utiliza una estrategia de "divide y conquista". Se elige un elemento llamado pivote y se divide el arreglo en dos subarreglos: uno con elementos menores al pivote y otro con elementos mayores. Luego se ordenan recursivamente los subarreglos y se combinan para obtener el arreglo ordenado.

El código utiliza la biblioteca zmq para la comunicación entre procesos y la biblioteca random para generar números aleatorios.

Tambien se implementa un menú de opciones para el usuario, donde se le pide que seleccione uno de los tres algoritmos de ordenamiento disponibles (mergesort, heapsort o quicksort) o salir del programa. 

El código utiliza un bucle `while True` para mostrar el menú de opciones y pedir al usuario que ingrese su elección. Si la elección del usuario es "1", "2" o "3", se le pide que ingrese el tamaño del vector a ordenar y se genera un vector aleatorio con números enteros entre 1 y 1000000. Luego, se utiliza ZeroMQ para enviar el vector a un proceso worker que implementa el algoritmo de ordenamiento seleccionado por el usuario. Una vez que el worker termina de ordenar el vector, envía el vector ordenado y el tiempo total que tardó en ordenarlo de vuelta al proceso principal. El proceso principal muestra el vector ordenado y el tiempo total en la pantalla. 

Si la elección del usuario es "4", el programa sale del bucle `while True` y muestra un mensaje de despedida. Si la elección del usuario no es válida, se le pide que ingrese una opción válida y se muestra el menú de opciones nuevamente.