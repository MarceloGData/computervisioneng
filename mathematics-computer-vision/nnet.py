import numpy as np


def generate_wt(a, b):
    random_values = [np.random.randn() for _ in range(a * b)]
    generated_array = np.asarray(random_values).reshape(a, b)
    return generated_array


##############################
#### generate weights ########
##############################

w1 = generate_wt(3, 4)
b1 = generate_wt(1, 4)

w2 = generate_wt(4, 1)
b2 = generate_wt(1, 1)

##############################
##############################


x = [0, 1, 2]

h = np.add(np.matmul(x, w1), b1)  # x.w1 + b1

y = np.add(np.matmul(h, w2), b2)  # h.w2 + b2

print(y)

##############################
##############################
