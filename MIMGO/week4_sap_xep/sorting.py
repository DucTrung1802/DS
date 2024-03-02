import numpy as np


def calc_sums(x):
    return (np.sum(x), np.sum(x, axis=0), np.sum(x, axis=1))


# hello = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# calc_sums(hello)