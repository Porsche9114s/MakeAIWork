#!/usr/bin/python3
#Multiplicate 2 vectors and use a forloop

class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
        
        #pass
    def multiply(self,matrixb):
        for rowIndex in range(len(self.matrix)):
            for columIndex in range(len(matrixb[0])):
                for termIndex in range(len(self.matrix[0])):
                    result[rowIndex][columIndex] += self.matrix[rowIndex][termIndex] * matrixb [termIndex][columIndex]
        return result
        #for row in result:

jantje  = [[4, 0, 3],[1, -1, 7],[-3, 3, 2]]
pietje = [[-2, 3, 1],[2,-3,-5],[4, 0, 7]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


clmat = Matrix(jantje)
#print(clmat)
#print(clmat.matrix)
resultaten = clmat.multiply(pietje)
print(resultaten)           

