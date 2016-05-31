from munkres import Munkres, print_matrix, make_cost_matrix
import sys
from math import log10

matrix = [[1, 0.003, 0.1938, 0.0021, 0.0027],
          [331.5, 1, 69.2387, 0.6955, 0.9109],
          [5.16, 0.0144, 1, 0.0107, 0.014],
          [483.85, 1.4379, 93.7694, 1, 1.2855],
          [376.4, 1.0978, 71.5891, 0.7779, 1]]


def convert_matrix_to_log(matrix):
    new_matrix = []

    for list in matrix:
        new_row=[]
        for element in list:
            new_row.append(log10(element))
        new_matrix.append(new_row)
    return new_matrix

mat = convert_matrix_to_log(matrix)
print(mat)
cost_matrix = make_cost_matrix(mat, lambda cost: sys.maxsize - cost)
m = Munkres()
indexes = m.compute(cost_matrix)
# print_matrix(matrix, msg='The maximum length contour is:')
total = 0
for row, column in indexes:
    value = mat[row][column]
    total += value
    print('(%d, %d) -> %f' % (row, column, value))

print('total profit=%f' % total)

