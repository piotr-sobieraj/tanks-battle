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
    
    # Main game loop
    while not board.isGameOver():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit

        board.updateDistanceInfo()
        # Tactics of the red tank - should be put in the fight method.
        redTank.rotate(45)
        redTank.move(20)
        
        # board.distanceBetweenTanks()
        # Tactics of the white tank 
        whiteTank.fight()
        # board.distanceBetweenTanks()
    
        # Detection of a hit.
        if (Tank.detectHit(redTank, whiteTank)):
            board.addPointsTo(redTank)
        elif Tank.detectHit(whiteTank, redTank):
            board.addPointsTo(whiteTank)

        # board.calcDistanceBetweenTanks()
        # print(board.distanceBetweenTanks)
        board.redraw()    
        board.slowDown()