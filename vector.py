import random
import zmq

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
        print(vector)
        print("-----------------------------------------")
        # Configurar el contexto de ZeroMQ
        context = zmq.Context()

        # Configurar el socket para enviar el vector al primer worker
        worker_socket = context.socket(zmq.REQ)
        worker_socket.connect("tcp://127.0.0.1:5555")
        problem = {
            'algorithm': 'mergesort',
            'vector': vector
        }

        # Enviar vector al primer worker
        worker_socket.send_json(problem)


        # Recibir vector ordenado del último worker
        response = worker_socket.recv_json()

        # Obtener el vector ordenado y el tiempo total de la respuesta
        sorted_vector = response['sorted_vector']
        elapsed_time = response['elapsed_time']

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
        worker_socket.connect("tcp://127.0.0.1:5555")
        problem = {
            'algorithm': 'heapsort',
            'vector': vector
        }
        # Enviar vector al primer worker
        worker_socket.send_json(problem)


         # Recibir vector ordenado del último worker
        response = worker_socket.recv_json()

        # Obtener el vector ordenado y el tiempo total de la respuesta
        sorted_vector = response['sorted_vector']
        elapsed_time = response['elapsed_time']

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
        worker_socket.connect("tcp://127.0.0.1:5555")
        print("conec")
        problem = {
            'algorithm': 'quicksort',
            'vector': vector,
            'pivot_choice': pivot_choice
        }
        # Enviar vector al primer worker
        worker_socket.send_json(problem)
        print("envia")

        # Recibir vector ordenado del último worker
        response = worker_socket.recv_json()
        print("recibe")

        # Obtener el vector ordenado y el tiempo total de la respuesta
        sorted_vector = response['sorted_vector']
        elapsed_time = response['elapsed_time']

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

