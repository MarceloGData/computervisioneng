import numpy as np


P = np.asarray([
    [1, 3, -2],
    [0, 2, 4]
])

Q = np.asarray([
    [4, 0],
    [2, -3],
    [1, -2]
])

print(np.matmul(P, Q))
