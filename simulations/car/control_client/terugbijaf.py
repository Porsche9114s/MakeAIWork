from tensorflow import keras
import numpy as np
import pandas as pd
#Trainingset laden
#dataframe = pd.read_csv('C:/Users/vande/makeaiwork/simulations/car/control_client/sonar.samples',  header = None, sep = ' ')
dataframe = pd.read_csv('./simulations/car/control_client/sonar.samples',  header = None, sep = ' ')
#dataframe omzetten
numpyarray = np.array(dataframe)
distances = []
steering = []
for x in numpyarray:
    distancesSonar = float(x[0].split(',')[0]), float(x[0].split(',')[1]), float(x[0].split(',')[2])
    steeringSonar =  float(x[0].split(',')[3])
    data_np = np.asarray(distancesSonar, np.float32)
    #s = tf.convert_to_tensor(data_np, np.float32)
    distances.append(distancesSonar)
    steering.append(steeringSonar)

# Validation data 0 - 299
val_distances = np.array(distances[0:299])
val_steering = np.array(steering[0:299])

#neural network, Tensorflow input, layers en output
inputs = keras.Input(shape=(3,), name="distances_input")
x = keras.layers.Dense(16, activation="relu",)(inputs)
x = keras.layers.Dense(32, activation="relu",)(x)
x = keras.layers.Dense(16, activation="relu",)(x)
output = keras.layers.Dense(1, name="predictions")(x)
model = keras.Model(inputs=inputs, outputs=output, name="3_layer_mlp")

#model afstellen, let op learningrate. Standaard op 0.001
model.compile(optimizer='adam', loss='MeanSquaredError', metrics=['accuracy'])

#model trainen
model.fit(distances, steering, epochs=500)

#opslaan model
model.save('simulations/car/control_client/Opdracht/ai/model')

#weergeven resultaten.
test_loss, test_acc = model.evaluate(val_distances, val_steering, verbose=2)
print('\nvalidation Accuracy:', test_acc, '\nValidation loss:', test_loss)

# steering output
predictions = model.predict(np.array(val_distances))
print(np.round(predictions))
