import numpy as np
import random


def play_random(board):
    print(board)
    nan_indices = np.argwhere(np.isnan(board))
    row, col = random.choice(nan_indices)
    print(row, col)

    return row, col


def play_and_learn(board):
    non_nan_indices = np.argwhere(np.invert(np.isnan(board)))
    nan_indices = np.argwhere(np.isnan(board))
    indices = np.arange(nan_indices.shape[1])

    prob = np.random.rand(*board.shape)

    for row, col in non_nan_indices:
        print(prob)
        print(row, col)
        prob[row][col] = 0

    prob /= np.sum(prob)
    row, col = nan_indices[np.random.choice(indices, p=prob.flatten())]

    print(row, col)
    return row, col
