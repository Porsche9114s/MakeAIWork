#!/usr/bin/env python
from tensorflow import keras
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)


# Model inladen in TensorFlow
#model = 'simulations/car/control_client/Opdracht/AI/model'
model = keras.models.load_model('simulations/car/control_client/sonar_test.csv')

# testdata laden
#dataset = pd.read_csv('simulations/car/control_client/sonar_test.csv')

#weergeven resultaten.
test_loss, test_acc = model.evaluate(y, x, verbose=2)

# steering output
predictions = model.predict(np.array(y))
print(np.round_(predictions))

