import numpy as np

import pandas as pd


dataframe = pd.read_csv('C:/Users/vande/MakeAIWork/simulations/car/control_client/sonar.csv', header = None, sep = ' ')

#dataframe.to_csv('C:/Users/vande/MakeAIWork/simulations/car/control_client/sonar.csv', header = ["dist1","dist2","dist3","angle"], index=False)

#print (dataframe.head)

#print (dataframe.shape)

numpyarray = np.array(dataframe)

for x in numpyarray:
    print (x[0].split(',') [0] + " | " + x[0].split(',')[1] + " | " + x[0].split(',')[2])
     
