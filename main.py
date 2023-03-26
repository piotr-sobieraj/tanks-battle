import pygame
import constants as const
from tank import Tank
from board import Board

if __name__ == "__main__":
    
    # Create tanks
    redTank = Tank(const.red)
    whiteTank = Tank(const.white)
    
    # Board with two tanks on it
    board = Board(redTank, whiteTank)        

    redTank.rotate(30)
    redTank.rotate(30)
    redTank.rotate(30)
    redTank.rotate(30)
    redTank.rotate(30)
    redTank.rotate(30)
    redTank.rotate(30)
    
    
    
    board.updateAngleInfo()
    print(f"{redTank.angleToOpponent=}, {whiteTank.angleToOpponent=}")
    board.redraw()