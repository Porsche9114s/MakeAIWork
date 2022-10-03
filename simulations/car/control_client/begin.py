import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt



dataset = pd.read_csv('C:/Users/vande/MakeAIWork/simulations/car/control_client/sonar.csv')
# get all headers in csv
values = list(dataset.columns.values)

# get the labels, assuming last row is labels in csv
y = dataset[values[0:3]]
y = np.array(y, dtype='float32')
X = dataset[values[3]]
X = np.array(X, dtype='float32')

#print (X)
#print (y)
print(np.shape(x))
print(np.shape(y))
