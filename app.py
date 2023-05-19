from flask import Flask, render_template, request
import random
import zmq

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        vector_size = int(request.form['vector-size'])
        vector = [random.randint(1, 1000000) for _ in range(vector_size)]
        print(vector)    
        sorted_vector = None  # Variable para almacenar el vector ordenado
        pivot_choice = None  # Variable para almacenar la selección del pivote

        if 'sort-quick' in request.form:
            if 'pivot-choice' in request.form:
                pivot_choice = request.form['pivot-choice']
            return render_template('index.html', button_name='QuickSort', vector=vector, sorted_vector=sorted_vector, pivot_choice=pivot_choice)

        elif 'sort-heap' in request.form:
            button_name = 'HeapSort'
            # Configurar el contexto de ZeroMQ
            context = zmq.Context()

            # Configurar el socket para enviar el vector al primer worker
            worker_socket = context.socket(zmq.REQ)
            
            worker_socket.connect("tcp://127.0.0.1:5555")
            print("Conectado al worker.")
            problem = {
                'algorithm': 'heapsort',
                'vector': vector
            }
            # Enviar vector al primer worker
            worker_socket.send_json(problem)
            print("Vector enviado al worker.")


            # Recibir vector ordenado del último worker
            response = worker_socket.recv_json()
            print("Respuesta recibida del worker.")

            # Obtener el vector ordenado y el tiempo total de la respuesta
            sorted_vector = response['sorted_vector']
            elapsed_time = response['elapsed_time']

            # Cerrar el socket del worker
            worker_socket.close()
            print("Socket del worker cerrado.")
            print("Vector ordenado:", sorted_vector)
            print("Tiempo total:", elapsed_time)
            print()
        elif 'sort-merge' in request.form:
            button_name = 'MergeSort'
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
            print("Socket del worker cerrado.")
            print("Vector ordenado:", sorted_vector)
            print("Tiempo total:", elapsed_time)
            print()
        else:
            button_name = ''
        return render_template('index.html', button_name=button_name, vector=vector, sorted_vector=sorted_vector)

    return render_template('index.html')

def perform_quicksort(vector, pivot_choice):
    # Aquí realizas el proceso de ordenamiento con QuickSort
    # y retornas el vector ordenado
    pass

if __name__ == '__main__':
    app.run(debug=True)

