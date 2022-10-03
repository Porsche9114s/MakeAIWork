
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataframe = pd.read_csv('C:/Users/vande/makeaiwork/simulations/car/control_client/sonar.samples',  header = None, sep = ' ')
dataframe.to_csv('C:/Users/vande/makeaiwork/simulations/car/control_client/sonar.samples', header = None, index=False)


# Trainset laden
#dataset = pd.read_csv('simulations/car/control_client/sonar_train.csv')
#data fram omzetten
numpyarray = np.array(dataframe)
arr_distances = []
arr_steering = []
for x in numpyarray:
    distancesSonar = float(x[0].split(',')[0]), float(x[0].split(',')[1]), float(x[0].split(',')[2])
    steeringSonar =  float(x[0].split(',')[3])
    data_np = np.asarray(distancesSonar, np.float32)
    s = tf.convert_to_tensor(data_np, np.float32)
    arr_distances.append(distancesSonar)
    arr_steering.append(steeringSonar)

#y = dataset[values[0:3]]
#y = np.array(y, dtype='float32')
#x = dataset[values[3]]
#x = np.array(x, dtype='float32')

val_arr_distances = np.array(arr_distances[0:299])
val_arr_steering = np.array(arr_steering[0:299])
#print(np.shape(x))
#print(np.shape(y))

# Validation data 0 - 299
#val_arr_distances = np.array([0:299])
#val_arr_steering = np.array([0:299])

#neural network
#tensorflow input
#aantal layers
#output.

#Tensorflow input, layers en output
inputs = keras.Input(shape=(3,), name="distances_input")
x = keras.layers.Dense(16, activation="relu", name="layer_1")(inputs)
x = keras.layers.Dense(32, activation="relu", name="layer_2")(x)
x = keras.layers.Dense(16, activation="relu", name="layer_3")(x)
output = keras.layers.Dense(1, name="predictions")(x)
model = keras.Model(inputs=inputs, outputs=output, name="3_layer_mlp")

#model = tf.keras.Sequential([
#    tf.keras.layers.Dense (3, input_shape=(3, )),
#    tf.keras.layers.Dense(16, activation='relu'),
#    tf.keras.layers.Dense(32, activation='relu'),
#    tf.keras.layers.Dense(16, activation='relu'),
#    tf.keras.layers.Dense(1,)])


#model afstellen
#let op learningrate. Standaard op 0.001
model.compile(optimizer='adam',
loss='MeanSquaredError',
metrics=['accuracy'])



#model trainen
model.fit(arr_distances, arr_steering, epochs=100)

#opslaan model
model.save('simulations/car/control_client/Opdracht/ai/model')

#weergeven resultaten.
test_loss, test_acc = model.evaluate(val_arr_distances, val_arr_steering, verbose=2)
print('\nvalidation Accuracy:', test_acc, '\nValidation loss:', test_loss)
# steering output
predictions = model.predict(np.array(val_arr_distances))
print(np.round(predictions))
