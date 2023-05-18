from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        vector_size = int(request.form['vector-size'])
        vector = [random.randint(1, 1000000) for _ in range(vector_size)]
        n = vector
        return render_template('index.html', vector=vector)
        
    return render_template('index.html')
if __name__== '__main__':
    app.run(debug=True)#Cambiar luego

