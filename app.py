import numpy as np
import cv2
import tensorflow as tf
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

# Inicializar Flask
app = Flask(__name__)
CORS(app)

# Cargar el modelo
model = tf.keras.models.load_model('./best_model.h5')

# Definir las categorías
categories = ['violeta', 'rojo', 'azul', 'verde', 'negro', 'marrón', 'blanco']
img_size = 128  # Tamaño de las imágenes utilizado durante el entrenamiento

# Función asincrónica para predecir el color
async def predict_color(file):
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    img_resized = cv2.resize(img, (img_size, img_size))
    img_normalized = img_resized / 255.0
    img_reshaped = img_normalized.reshape(1, img_size, img_size, 3)
    prediction = model.predict(img_reshaped)
    predicted_color = categories[np.argmax(prediction)]
    return predicted_color

# Ruta para predecir el color
@app.route('/predict', methods=['POST'])
async def predict():
    file = request.files['file']
    
    # Manejar la predicción de manera asincrónica
    predicted_color = await predict_color(file)
    
    return jsonify({'color': predicted_color})

# Ruta para la página HTML
@app.route('/')
def index():
    return send_from_directory('', 'reconocimientoDeColores.html')

if __name__ == '__main__':
    app.run(debug=True)
