

# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

import pandas as pd
import numpy as np
from tensorflow import keras



# Trainset laden
dataset = pd.read_csv('simulations/car/control_client/sonar_train.csv')

#let op; zijn het values of columns
#conversie van Data uit CSV bestand
values = list(dataset.columns.values)

y = dataset[values[0:3]]
y = np.array(y, dtype='float32')
x = dataset[values[3]]
x = np.array(x, dtype='float32')


print(np.shape(x))
print(np.shape(y))
#print (x)
#print (y)

# Validation data 0 - 299
#val_arr_distances = np.array(y[0:299])
#val_arr_steering = np.array(x[0:299])




#neural network
#tensorflow input
#aantal layers
#output.

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

#opslaan model

model.save('simulations/car/control_client/sonar_test')
#from tensorflow import keras


# Model inladen in TensorFlow
#model = 'simulations/car/control_client/Opdracht/AI/model'
#model = keras.models.load_model('simulations/car/control_client/sonar_test.csv')

# testdata laden
#dataset = pd.read_csv('simulations/car/control_client/sonar_test.csv')

#weergeven resultaten.
test_loss, test_acc = model.evaluate(y, x, verbose=2)

# steering output
predictions = model.predict(np.array(y))
print(predictions)

