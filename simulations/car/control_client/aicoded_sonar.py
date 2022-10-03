from cgi import print_directory
import numpy as np
import pandas as pd
from matplotlib import pyplot 
import tensorflow as tf
from tensorflow import keras

dataframe = pd.read_csv('C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/AI/Sonar/sonar.samples', header = None, sep = ' ')
dataframe.to_csv('C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/AI/Sonar/sonar.samples', header = None, index=False)
#print (np.array(dataframe))
#print (df.shape)


# Dataframe conversion
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


# Validation data 0 - 299
val_arr_distances = np.array(arr_distances[0:299])
val_arr_steering = np.array(arr_steering[0:299])


#Tensorflow input, layers en output
inputs = keras.Input(shape=(3,), name="distances_input")
x = keras.layers.Dense(16, activation="relu", name="layer_1")(inputs)
x = keras.layers.Dense(32, activation="relu", name="layer_2")(x)
x = keras.layers.Dense(16, activation="relu", name="layer_3")(x)
output = keras.layers.Dense(1, name="predictions")(x)
model = keras.Model(inputs=inputs, outputs=output, name="3_layer_mlp")


# Compiler
model.compile(
optimizer='adam',
loss='mean_squared_error',
metrics=[
    'accuracy', #tf.keras.losses.MeanSquaredError() 'mean_squared_error'
    
]) 


# aantal epochs om te trainen
model.fit(arr_distances, arr_steering, epochs=100)

# opslaan van model
model.save('C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/AI/model')

# (functie evaluate) Validation om de data te controleren dat het overeenkomt met de resultaat (testset)
test_loss, test_acc = model.evaluate(val_arr_distances,  val_arr_steering, verbose=2)
print('\nValidation Accuracy:', test_acc, '\nValidation loss:', test_loss)


#steering output
prediction = model.predict(np.array(val_arr_distances))
print(np.round_(prediction))


# Bekijk je prediction op rieele waarden
# pyplot.figure()
# pyplot.plot(val_arr_steering)
# pyplot.plot(prediction,'r')
# pyplot.show()















# lf = tf.keras.losses.mean_squared_error










# lb = LabelEncoder()

# # trainLabels = lb.fit_transform(output)

# testLabels = lb.fit_transform(test_arr_steering)

# validLabels = lb.fit_transform(val_arr_steering)

# labels = []
# for x in validLabels:
#     if x == 0:
#         labels.append(-22)
#     elif x == 1:
#         labels.append(0)
#     elif x == 2:
#         labels.append(22)



# probability_model = tf.keras.Sequential([model, 
#                                          tf.keras.layers.Softmax()])

# prediction = probability_model.predict(val_arr_distances)

# print(prediction)
# for i in prediction:
#     if i[0] > i[1] and  i[2]:
#         print(-22)
#     elif i[1] > i[0] and  i[0]:
#         print(0)
#     elif i[2] > i[1] and  i[0]:
#         print(22)



# De overfit voorkomen (functie evaluate) Validation om de data te controleren dat het overeenkomt met de resultaat (testset)
# Stuurhoeken normaliseren en linken aan werkelijke stuurhoeken ,prediction 
# Implementatie met hardcoded