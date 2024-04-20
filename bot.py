import numpy as np
import random
import brain


def play_random(board):
    print(board)
    nan_indices = np.argwhere(np.isnan(board))
    row, col = random.choice(nan_indices)
    print(row, col)

    return row, col

def see(board):
    vision = []
    for row in board:
        for square in row:
            print(square)
            res = 0
            if square == 1:
                res = 1
            if square == 0:
                res = -1
            
            vision.append(res)


    print(vision)
    return vision

def play_but_with_brain(board, neural_network):
    vision = see(board)

    b = []
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            b.append([i,j])
    indices = np.array(b)

    
    prediction = neural_network.predict(vision)
    


    prediction /= np.sum(prediction)
    print(indices)
    print()

    
    row, col = indices[np.random.choice(range(board.size), p=prediction.flatten())]

    print(row, col)
    return row, col



def play_random_but_with_prob(board):
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
