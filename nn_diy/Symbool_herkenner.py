trainingset = ( ((1,1,1),   
                (1,0,1),
                (1,1,1),)  
              )

def matrix2vector(mat):
    vec= []

    for row in mat:
        for val in row:

            vec.append(val)

    return vec

outvector = matrix2vector(trainingset)

vec = [1,2,3]

def weights(vector,weightvalue):
    
    n = len(vector)

    weight=[]
    for a in range(0,n):
        weight.append(weightvalue)
    return weight

weightlist = weights(outvector,1.1)

def multiply(vector,weightlist):
    #print(vector)
    #print(weightlist)
    
    n=len(vector)



    result=0
    for a in range(0,n):
        #result += vector[a] * weightlist[a]
        result = result+ vector[a] * weightlist[a]
    return result

result = multiply(outvector,weightlist)


'''
We hebben een Matrix omgezet naar een vector. (node)
We hebben de weight functie aangemaakt en die kunnen we vermenigvuldigen met de waarde(weightlist) 1.1).
lijnen 0 t/m 8 (weights)

Tot zo ver zijn we min of meer.

Nu moeten we de uitkomst vertalen naar softmax functie over de uitkomst van de berekening halen.

de uitkomst van softmax  een mean squared error. deze waarde geeft een indicatie over de betrouwbaarheid.
Je weet wat de uitkomst moet zijn van de gegeven (training) matrixen  (een nul of een X). 100 %

De uitslagen van de Testmatrixen kan je hiermee vergelijken en dan aangeven hoe waarschijnlijk het is dat het een X of een 0 is.




# transform values into probabilities
from math import exp
# calculate each probability
p1 = exp(1) / (exp(1) + exp(3) + exp(2))
p2 = exp(3) / (exp(1) + exp(3) + exp(2))
p3 = exp(2) / (exp(1) + exp(3) + exp(2))
# report probabilities
print(p1, p2, p3)
# report sum of probabilities
print(p1 + p2 + p3)





'''

#print(weightlist)
#print(trainingset)
#print(weights)

#print(outvector)
#print(weightlist)
#print(weightvalue)
#weightlist = weights(vec)
#weightlist = weightlist(vec)







