''' 
Neural net bouwen en trainen.
Tensorflow is de toolkit voor machinelearning
tf.keras tensorflow
preprogres data
shape data in 3,1
First layer
Activatie softmax laatste laag uitkomst tussen 0 en 1
splitsen in uitkomsten 0 tot 0,5 en 0,5 en 1.
Dense = fully connected
1e layer 3
2e layer 8
3e layer 8

activatie is 1
is softmax

loss means square error

model fit.

tensorflow.org/tutorials/keras/classification

'''
# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

import pandas as pd
import numpy as np

dataset = pd.read_csv('C:/Users/vande/MakeAIWork/simulations/car/control_client/sonar.csv')

#let op; zijn het values of columns
values = list(dataset.columns.values)

y = dataset[values[0:3]]
y = np.array(y, dtype='float32')
x = dataset[values[3]]
x = np.array(x, dtype='float32')

print(np.shape(x))
print(np.shape(y))
#print (x)
#print (y)


#neural network
model = tf.keras.Sequential([
    tf.keras.layers.Dense (3, input_shape=(3, )),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1,)])


#model afstellen
#let op learningrate. Standaard op 0.001
model.compile(optimizer='adam',
loss=tf.keras.losses.MeanSquaredError(),
metrics=['accuracy'])



#model trainen
model.fit(y, x, epochs=250)


#weergeven resultaten.
test_loss, test_acc = model.evaluate(y, x, verbose=2)

#print('\nTest accuracy:', test_acc)

#probability_model = tf.keras.Sequential([model, 
#tf.keras.layers.Softmax()])

predictions = model.predict(y)
#np.argmax(predictions[0])
print(predictions)