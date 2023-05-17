import random
import zmq

def mergesort(arr):
    """
    Ordena un arreglo de manera ascendente utilizando el algoritmo de mergesort.

    Args:
        arr (list): El arreglo a ordenar.

    Returns:
        list: El arreglo ordenado.

    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Combina dos arreglos ordenados en un solo arreglo ordenado.

    Args:
        left (list): El primer arreglo ordenado.
        right (list): El segundo arreglo ordenado.

    Returns:
        list: El arreglo combinado y ordenado.

    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heapsort(arr):
    """
    Ordena un arreglo de manera ascendente utilizando el algoritmo de heapsort.

    Args:
        arr (list): El arreglo a ordenar.

    """
    build_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

def build_heap(arr):
    """
    Construye un heap a partir de un arreglo dado.

    Args:
        arr (list): El arreglo para construir el heap.

    """
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, i, n)

def heapify(arr, i, n):
    """
    Aplica la operación de heapify en un subárbol de un heap.

    Args:
        arr (list): El arreglo que representa el heap.
        i (int): Índice del nodo raíz del subárbol.
        n (int): Tamaño del heap.

    """
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)

def quicksort(arr, start, end, pivot_choice):
    """
    Ordena un vector utilizando el algoritmo de Quicksort de manera recursiva.

    Args:
        arr (list): El vector a ser ordenado.
        start (int): El índice de inicio del rango a ordenar.
        end (int): El índice de fin del rango a ordenar.
        pivot_choice (str): La elección del pivote inicial ("left" o "right").

    Returns:
        None

    Raises:
        None
    """
    if start < end:
        if pivot_choice == "left":
            pivot_idx = start
        elif pivot_choice == "right":
            pivot_idx = end
        else:
            raise ValueError("La opción de pivote es inválida. Por favor, seleccione 'left' o 'right'.")

        pivot = arr[pivot_idx]
        i = start
        j = end
        while i <= j:
            while i <= end and arr[i] <= pivot:
                i += 1
            while j >= start and arr[j] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[pivot_idx], arr[j] = arr[j], arr[pivot_idx]
        pivot_idx = j

        quicksort(arr, start, pivot_idx - 1, pivot_choice)
        quicksort(arr, pivot_idx + 1, end, pivot_choice)
        

# Generar vector aleatorio
while True:
    print("------ Menú de Ordenamiento ------")
    print("1. Ordenar utilizando Mergesort")
    print("2. Ordenar utilizando Heapsort")
    print("3. Ordenar utilizando Quicksort")
    print("4. Salir")
    
    choice = input("Ingrese el número de opción: ")
    
    if choice == "1":
        n = int(input("Ingrese el tamaño del vector: "))
        vector = [random.randint(1, 1000000) for _ in range(n)]

        # Configurar el contexto de ZeroMQ
        context = zmq.Context()

        # Configurar el socket para enviar el vector al primer worker
        worker_socket = context.socket(zmq.REQ)
        worker_socket.connect("tcp://localhost:5555")

        # Enviar vector al primer worker
        worker_socket.send_json(vector)

        # Recibir vector ordenado del último worker
        sorted_vector = worker_socket.recv_json()

        # Recibir tiempo total del último worker
        elapsed_time = float(worker_socket.recv())

        # Cerrar el socket del worker
        worker_socket.close()

        print("Vector ordenado:", sorted_vector)
        print("Tiempo total:", elapsed_time)
        print()
        
    elif choice == "2":
        n = int(input("Ingrese el tamaño del vector: "))
        vector = [random.randint(1, 1000000) for _ in range(n)]

        # Configurar el contexto de ZeroMQ
        context = zmq.Context()

        # Configurar el socket para enviar el vector al primer worker
        worker_socket = context.socket(zmq.REQ)
        worker_socket.connect("tcp://localhost:5555")

        # Enviar vector al primer worker
        worker_socket.send_json(vector)

        # Recibir vector ordenado del último worker
        sorted_vector = worker_socket.recv_json()

        # Recibir tiempo total del último worker
        elapsed_time = float(worker_socket.recv())

        # Cerrar el socket del worker
        worker_socket.close()

        print("Vector ordenado:", sorted_vector)
        print("Tiempo total:", elapsed_time)
        print()
        
    elif choice == "3":
        n = int(input("Ingrese el tamaño del vector: "))
        vector = [random.randint(1, 1000000) for _ in range(n)]
        pivot_choice = input("Seleccione el pivote inicial (left/right): ")

        # Configurar el contexto de ZeroMQ
        context = zmq.Context()

        # Configurar el socket para enviar el vector al primer worker
        worker_socket = context.socket(zmq.REQ)
        worker_socket.connect("tcp://localhost:5555")

        # Enviar vector al primer worker
        worker_socket.send_json(vector)

        # Recibir vector ordenado del último worker
        sorted_vector = worker_socket.recv_json()

        # Recibir tiempo total del último worker
        elapsed_time = float(worker_socket.recv())

        # Cerrar el socket del worker
        worker_socket.close()

        print("Vector ordenado:", sorted_vector)
        print("Tiempo total:", elapsed_time)
        print()
        
    elif choice == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número de opción válido.")
        print()

