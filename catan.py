#!/usr/bin/python

"""
catan.py

A module to handle the catan board generation and states.
"""

import numpy as np
import random

class Board():
    """
    Generate a catan board, handle player positions, hex numbering and 
    resources, and robber positions.
    """

    def __init__(self, radius = 2):
        """
        Generate the board.
        """

        # Radius of the board
        self.radius = radius

        # Generate the resources and numbering
        self.generateResources() 
        self.generateNumbering()        
        self.vertices = np.zeros((self.radius*2 + 1, self.radius*2 + 1,6))
        self.edges = np.zeros((self.radius*2 + 1, self.radius*2 + 1,6))

    def __str__(self):
        string = ""
        resourceColors = ["\x1B[30m",#black
                          "\x1B[38m",#black
                          "\x1B[34m",#grey
                          "\x1B[31m",#red
                          "\x1B[32m",#green
                          "\x1B[37m",#white
                          "\x1B[33m"#yellow
                          ]
        for row in range(0,self.radius*2 +1):
            for col in range(0,self.radius*2 +1):
                resource = self.resources[row,col]
                number = int(self.numbers[row,col])
                string += " {0} {1: <3}\x1B[0m".format(resourceColors[int(resource)],number)
            string += "\n"

        return string

    def generateResources(self):
        """
        Add resources to the map.
        """
        self.resources = np.zeros((self.radius*2 + 1,self.radius * 2 + 1))

        resourceList = [ 1,2,2,2,
                         3,3,3,
                         4,4,4,4,
                         5,5,5,5,
                         6,6,6,6]
        random.shuffle(resourceList)
        for r in range(-self.radius,self.radius+1):
            for q in range(-self.radius,self.radius+1):
                firstColumn = - self.radius -min(0,r)
                row, col = axialToMatrix(q,r,self.radius)
                if col >= 0 and row >= 0 and -self.radius <= q+r <= self.radius:
                    self.resources[row,col] = resourceList.pop()



    def generateNumbering(self):
        """
        Add nubering to the hex.
        """

        numberList = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
        random.shuffle(numberList)

        self.numbers = np.zeros((self.radius*2 + 1,self.radius * 2 + 1))
        for r in range(-2,3):
            for q in range(-2,3):

                row,col = axialToMatrix(q,r,self.radius)
                
                # Check for desert
                if self.resources[row,col] > 1:
                    self.numbers[row,col] = numberList.pop()

    

# General Functions

def axialToMatrix(q,r,radius):
    """
    Convert axial coordinates to matrix coordinates.
    """
    row = r + radius 
    col = q+radius+min(0,r)

    return (row,col)


def main():
    """
    Testing function to generate a board and to update the map.
    """

    board = Board()
    print(board)


if __name__ == "__main__":
    main()
