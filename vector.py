import random

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
    Ordena un arreglo de manera ascendente utilizando el algoritmo de quicksort.

    Args:
        arr (list): El arreglo a ordenar.
        start (int): Índice de inicio del segmento a ordenar.
        end (int): Índice de fin del segmento a ordenar.
        pivot_choice (str): Elección del pivote inicial ("left" o "right").

    """
    if start < end:
        if pivot_choice == "left":
            pivot_idx = start
        else:
            pivot_idx = end
        pivot = arr[pivot_idx]
        i = start
        j = end
        while i < j:
            while i < len(arr) and arr[i] <= pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[pivot_idx], arr[j] = arr[j], arr[pivot_idx]
        quicksort(arr, start, j-1, pivot_choice)
        quicksort(arr, j+1, end, pivot_choice)


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
        sorted_vector = mergesort(vector)
        print("Vector ordenado:", sorted_vector)
        print()
    elif choice == "2":
        n = int(input("Ingrese el tamaño del vector: "))
        vector = [random.randint(1, 1000000) for _ in range(n)]
        heapsort(vector)
        print("Vector ordenado:", vector)
        print()
    elif choice == "3":
        n = int(input("Ingrese el tamaño del vector: "))
        vector = [random.randint(1, 1000000) for _ in range(n)]
        pivot_choice = input("Seleccione el pivote inicial (left/right): ")
        quicksort(vector, 0, len(vector) - 1, pivot_choice)
        print("Vector ordenado:", vector)
        print()
    elif choice == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número de opción válido.")
        print()
