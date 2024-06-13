# ReconocimientoDeColores

Esta aplicación web utiliza un modelo de inteligencia artificial para predecir el color predominante en imágenes cargadas por el usuario. Desarrollada con Flask para el backend y JavaScript para el frontend.

## Instalación

Para ejecutar la aplicación localmente, sigue estos pasos:

### Requisitos Previos

Asegúrate de tener instalados los siguientes componentes:

- Python 3.x
. Node.js y npm (para desarrollo frontend, opcional si ya tienes el HTML y JS configurado)
  
### Pasos de Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/eric-escrich/ReconocimientoDeColores
   cd ReconocimientoDeColores
   ```

2. **Crear un Entorno Virtual**
   Este paso no es indispensable pero sí muy recomendable, sobretodo en el caso de Windows.
   
   * En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
     
    * En Linux o MacOS:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
      
4. **Instalar las dependencias de Python:**

   ```bash
   pip install tensorflow opencv-python-headless matplotlib flask flask-cors
   ```

   * **tensorflow:** Librería para cargar y utilizar el modelo de inteligencia artificial.
   * **opencv-python-headless:** Biblioteca para el procesamiento de imágenes.
   * **matplotlib:** Utilizado para mostrar gráficamente la imagen y el color predicho (opcional si solo se muestra en consola).
   * **flask y flask-cors:** Framework web y extensión para manejar solicitudes CORS en Flask.

5. **Descargar el modelo preentrenado:**

   Asegúrate de tener el modelo .h5 en la ruta especificada en el código Flask (app.py). Puedes descargar el modelo entrenado desde tu entorno de desarrollo o desde un servidor.

6. **Modificar el código según sea necesario:**

   * Verifica la ruta del modelo en app.py y asegúrate de que coincida con la ubicación de tu modelo descargado.
   * Si es necesario, ajusta las rutas en prediccionDeColores.html para asegurarte de que se están cargando correctamente los recursos estáticos.
  
## Ejecución

Una vez instaladas las dependencias y configurado el entorno, puedes ejecutar la aplicación:

```bash
python app.py
```

Esto iniciará el servidor Flask en http://127.0.0.1:5000/. Abre un navegador web y accede a esta dirección para usar la aplicación.

## Uso

1. **Carga de una imagen:**
   * Haz clic en el botón de selección de archivos.
   * Selecciona una imagen desde tu sistema de archivos.

2. **Predicción del color:**
   * Una vez que la imagen se carga en la interfaz, se mostrará en pantalla.
   * La aplicación enviará la imagen al servidor para la predicción.
   * El color predicho se mostrará debajo de la imagen o en la consola del navegador.

## Configuración del Modelo

* **Categorías de Colores:**
  La aplicación está configurada para predecir entre las siguientes categorías de colores: violeta, rojo, azul, verde, negro, marrón y blanco.
  
* **Tamaño de Imágenes:**
  El tamaño de las imágenes utilizado durante el entrenamiento del modelo es de 128x128 píxeles.

## Explicación

La aplicación utiliza un modelo de inteligencia artificial (IA) entrenado previamente para predecir el color predominante en una imagen. El modelo ha sido entrenado con diversas categorías de colores y utiliza técnicas de procesamiento de imágenes para normalizar y redimensionar las imágenes de entrada antes de realizar la predicción.
