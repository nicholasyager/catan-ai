#!/usr/bin/python3

from catan import catan
import numpy as np

# Dictionary of resources necessary for each action
development = { 
                'settlement' : [1,1,1,1,0], # Brick, Wood, Wheat, Sheep, Ore
                'city'       : [0,0,2,0,3],
                'development': [0,0,1,1,1],
                'road'       : [1,1,0,0,0]
              }

rollProbabilities = [0,0,0.0278,0.0556,0.0833,0.1111,0.1389,0.1667,0.1389,
                     0.1111,0.0833,0.0556,0.0278]

def calculateResourceProbability(board):
    """
    Calculate the probability of producing the board's resources this turn.
    """
    probabilities = np.zeros(board.shape)
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            number = int(board.numbers[row,col])
            if number < 0:
                number = 0
            probabilities[row,col] = rollProbabilities[number]

    print(probabilities)

def main():

    board = catan.Board()
    print(board)


    ## General steps of the game.
    ## For each turn, generate die role, choose the action that minimizes rolls
    ## to win, execute action if one exists.

    resourceProbability = calculateResourceProbability(board)

if __name__ == "__main__":
    main()
