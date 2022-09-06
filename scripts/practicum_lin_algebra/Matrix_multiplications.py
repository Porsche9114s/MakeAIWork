#!/usr/bin/python3
#Multiplicate 2 vectors and use a forloop

matrix_a = [[4, 0, 3],[1, -1, 7],[-3, 3, 2]]
matrix_b = [[-2, 3, 1],[2,-3,-5],[4, 0, 7]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for rowIndex in range(len(matrix_a)):
    for columIndex in range(len(matrix_b[0])):
        for termIndex in range(len(matrix_a[0])):
            result[rowIndex][columIndex] += matrix_a[rowIndex][termIndex] * matrix_b [termIndex][columIndex]

for row in result:
    print(row)


