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
    
    redTank.move(10)
    redTank.move(-10)
    redTank.rotate(10)
    redTank.move(-10)
    
    whiteTank.move(10)
    whiteTank.rotate(10)
    whiteTank.move(-10)    
    whiteTank.rotate(-10)
    
    
    # Main game loop
    while not board.isGameOver():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit

        board.UpdateInfo()
        redTank.fightRed()
        
        board.UpdateInfo()
        whiteTank.fightWhite()
    
        # Detection of a hit.
        if (Tank.detectHit(redTank, whiteTank)):
            board.addPointsTo(redTank)
        elif Tank.detectHit(whiteTank, redTank):
            board.addPointsTo(whiteTank)


        board.UpdateInfo()                
        board.redraw()                
        board.slowDown()   

