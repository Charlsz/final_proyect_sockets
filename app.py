from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Obtener el tamaño del vector enviado por el formulario
        vector_size = int(request.form['vector-size'])
        
        # Realizar el procesamiento y ordenación del vector aquí
        
        return render_template('resultado.html')  # Renderizar el template de resultado
        
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True)#Cambiar luego

