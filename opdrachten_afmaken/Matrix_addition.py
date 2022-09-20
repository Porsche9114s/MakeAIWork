#!/usr/bin/python3
#addition 2 vectors and use a forloop

#class Matrix:
#    def __init__(self,matrix):
#       self.matrix = matrix

jantje  = [[4, 0, 3],[1, -1, 7],[-3, 3, 2]]
pietje = [[-2, 3, 1],[2,-3,-5],[4, 0, 7]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



for plus in range(len(jantje)):
   
   for plus2 in range(len(jantje[0])):
       result[plus][plus2] = jantje[plus][plus2] + pietje[plus][plus2]

for antwoord in result:
   print(antwoord)
   



