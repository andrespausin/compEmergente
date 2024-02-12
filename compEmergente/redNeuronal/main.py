import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
from tensorflow import keras
import math

# Clasificador de imagenes de animales

# Categorias: Perro, Burro, Caballo, Oso, Mariposa

# Imagenes: 10 de cada categoria

# Total de imagenes: 100

# Las imagenes tendran una resolucion de 100x100 pixeles

# Se requieren 10000 datos de entrada y 10 datos de salida

# Dos capas ocultas de 50 neuronas cada una

datos, metadatos = tfds.load('imagenet_resized/64x64', as_supervised=True, with_info=True)

datos_entrenamiento, datos_pruebas = datos['train'], datos['test']

nombre_clases = metadatos.features['label'].names
print("Clases: ", nombre_clases)

def normalizar(imagenes, etiquetas):
    imagenes = tf.cast(imagenes, tf.float32)
    imagenes /= 255
    return imagenes, etiquetas

datos_entrenamiento = datos_entrenamiento.map(normalizar).cache()
datos_pruebas = datos_pruebas.map(normalizar).cache()

for imagen, etiqueta in datos_entrenamiento.take(1):
    break
imagen = imagen.numpy().reshape((64, 64, 3))

#dibujat
plt.figure
plt.imshow(imagen, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show()

plt.figure(figsize=(10, 10))
for i, (imagen, etiqueta) in enumerate(datos_entrenamiento.take(25)):
    imagen = imagen.numpy().reshape((64, 64, 3))
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(imagen, cmap=plt.cm.binary)
    plt.xlabel(nombre_clases[etiqueta])
plt.show()

modelo = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(64, 64, 3)),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

modelo.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

num_pasos_entrenamiento = metadatos.splits['train'].num_examples
num_pasos_pruebas = metadatos.splits['test'].num_examples

TAMANO_LOTE = 32
datos_entrenamiento = datos_entrenamiento.repeat().shuffle(num_pasos_entrenamiento).batch(TAMANO_LOTE)
datos_pruebas = datos_pruebas.batch(TAMANO_LOTE)

historial = modelo.fit(datos_entrenamiento, epochs=5, steps_per_epoch=math.ceil(num_pasos_entrenamiento/TAMANO_LOTE))