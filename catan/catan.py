#!/usr/bin/python

"""
catan.py

A module to handle the catan board generation and states.
"""

import numpy as np
import random

class Player:
    """
    A player has resources, roads, settlements, cities, development cards, and
    victory points. Players receive and spend resources, and place pieces.
    """
    
    numPlayers = 0;

    def __init__(self):
        # Add an ID to identify the player
        self.ID = numPlayers
        numPlayers += 1

class RoadError(Exception):
    """
    Raise this exception when you cannot place a road.
    """
    def __init__(self, message):
        self.message = message

class PositionError(Exception):
    """
    Raise this exception when you cannot place a city or settlement.
    """
    def __init__(self, message):
        self.message = message


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
        self.positions = np.zeros((self.radius*2 + 1, self.radius*2 + 1,6))
        self.roads = np.zeros((self.radius*2 + 1, self.radius*2 + 1,6))

        self.shape = self.resources.shape

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
                elif self.resources[row,col] == 1:
                    self.numbers[row,col] = -1 # Negative numbers denote robber

    def placeRoad(self,q,r,direction,ID):
        """
        This places a road on the map. The coordinates are q and r, and
        the direction of the road is determined by direction. The owner of the
        road is determined by ID.
        """
        row, col = axialToMatrix(q,r,self.radius)
        if self.roads[row,col,direction] == 0:
            self.roads[row,col,direction] = ID
        else:
            raise RoadException("Unable to place road at {0},{1},{2}".format(q,r,direction))

        

    def placeSettlement(self,q,r,direction,ID):
        """
        This places a settlement on the map. The coordinates are q and r, and
        the cardinal direction is determined by direction. The owner of the
        settlement is determined by ID.
        """
        row, col = axialToMatrix(q,r,self.radius)
        if self.positons[row,col,direction] == 0:
            self.positions[row,col,direction] = ID
        else:
            raise PostionException("Unable to place piece at {0},{1},{2}".format(q,r,direction))

        pass        

    def placeCity(self,q,r,direction,ID):
        """
        This places a city on the map. The coordinates are q and r, and
        the cardinal direction is determined by direction. The owner of the
        city is determined by ID.
        """
        
        row, col = axialToMatrix(q,r,self.radius)
        if self.positons[row,col,direction] == 0:
            self.positions[row,col,direction] = ID*10
        else:
            raise PostionException("Unable to place piece at {0},{1},{2}".format(q,r,direction))

        pass        


        pass        


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
