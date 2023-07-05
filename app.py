import numpy as np
from joblib import load
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

model = load('classification_clusters.joblib')

# render default webpage
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obter os dados de entrada
    data = request.json

    # Converter em 2D array
    data_array = np.array(list(data.values())).reshape(1, -1)

    # Realizar a previsão utilizando o modelo carregado
    prediction = model.predict(data_array)

    # Retornar a previsão como resposta
    response = {'prediction': int(prediction[0])}
    return jsonify(response)

# Definir as rotas e comportamentos da API.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



