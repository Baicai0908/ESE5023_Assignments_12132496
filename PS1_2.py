import numpy as np


def Matrix_multip(M1, M2):
    new_matrix = []
    for i in range(len(M1)):
        row = []
        for j in range(M2.shape[1]):
            result = 0
            for k in range(len(M1[i])):
                result += M1[i][k]*M2[k][j]
            row.append(result)
        new_matrix.append(row)
    print(new_matrix)

m1 = np.array(range(0, 50)).reshape(5, 10)
m2 = np.array(range(0, 50)).reshape(10, 5)
Matrix_multip(m1,m2)
