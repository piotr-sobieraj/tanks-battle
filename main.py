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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
        
        # Tactics of the red tank - should be put in the fight method.
        redTank.rotate(-15)
        redTank.move(10)
        
        # Tactics of the white tank - it should be always put in the fight method. 
        whiteTank.fight()
    
        # Detection of a hit.
        if (Tank.detectHit(redTank, whiteTank)):
            board.setCaption("White hit the red!")
        elif Tank.detectHit(whiteTank, redTank):
            board.setCaption("Red hit the white!")
        
        board.redraw()    
        board.slowDown()