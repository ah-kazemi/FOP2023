import numpy as np

matrices = []
with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    for i in range(n):
        matrix = np.fromfile(f, dtype=float, count=m*m, sep=' ').reshape(m, m)
        matrices.append(matrix)

max_det = -np.inf
max_matrices = None
for i in range(n):
    for j in range(i+1, n):
        det = np.linalg.det(np.dot(matrices[i], matrices[j]))
        if det > max_det:
            max_det = det
            max_matrices = (matrices[i], matrices[j])

if np.linalg.det(max_matrices[1]) > np.linalg.det(max_matrices[0]):
    result = np.linalg.inv(np.dot(max_matrices[1], max_matrices[0]))
else:
    result = np.linalg.inv(np.dot(max_matrices[0], max_matrices[1]))

result_list = result.tolist()
for row in result_list:
  print(' '.join(format(num, '.3f') for num in row))
