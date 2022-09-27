from pickletools import optimize
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dense
#from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam




model = keras.Sequential([
    Dense(units=8, input_shape=[1], activation = 'relu'),
    Dense(units=4, activation='relu')
])


model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], )
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], )

model.fit(xs, ys, epochs=2500)

print(model.predict([10.0]))
