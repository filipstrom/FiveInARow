import numpy as np
import random


def play_random(board):
    print(board)
    nan_indices = np.argwhere(np.isnan(board))
    row, col = random.choice(nan_indices)
    print(row, col)

    return row, col


def play_and_learn(board):
    b = []
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            b.append([i,j])
    indices = np.array(b)

    # Here is where the memory should be instead of a random each time
    prob = np.random.rand(*board.shape)

    prob[~np.isnan(board)] = 0

    prob /= np.sum(prob)
    print(indices)
    print()

    
    row, col = indices[np.random.choice(range(board.size), p=prob.flatten())]

    print(row, col)
    return row, col
