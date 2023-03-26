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


    # # Main game loop
    # while not board.isGameOver():
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit

    #     board.updateDistanceInfo()
    #     board.updateAngleInfo()
        
    #     # Tactics of the red tank - should be put in the fight method.
    #     redTank.rotate(20)
    #     redTank.move(20)
        
    #     board.updateDistanceInfo()
    #     board.updateAngleInfo()
        
    #     whiteTank.fight()
    
    #     # Detection of a hit.
    #     if (Tank.detectHit(redTank, whiteTank)):
    #         board.addPointsTo(redTank)
    #     elif Tank.detectHit(whiteTank, redTank):
    #         board.addPointsTo(whiteTank)

        
        
    #     board.redraw()    
    #     board.slowDown()