import pygame
import constants as const
from tank import Tank
from board import Board

if __name__ == "__main__":
    
    # Create tanks
    redTank = Tank(const.red, 100, 100)
    whiteTank = Tank(const.white, 350, 350)
            
    # Board with two tanks on it
    board = Board(redTank, whiteTank)        
    
    redTank.move(1)
    redTank.rotate(1)
    
    whiteTank.move(1)
    whiteTank.rotate(1)
    
    
    # Main game loop
    while not board.isGameOver():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit

        board.updateInfo()
        redTank.fightRed()
        
        board.updateInfo()
        whiteTank.fightWhite()
    
        # Detection of a hit.
        if (Tank.detectHit(redTank, whiteTank)):
            board.addPointsTo(redTank)
        elif Tank.detectHit(whiteTank, redTank):
            board.addPointsTo(whiteTank)


        board.redraw()                
        board.slowDown()   