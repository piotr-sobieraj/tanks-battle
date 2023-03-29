import pygame
import constants as const
from tank import Red, White, Tank
from board import Board

if __name__ == "__main__":
    
    # Create tanks
    Red = Red(const.red, 350, 350)
    White = White(const.white, 100, 100)
            
    # Board with two tanks on it
    board = Board(Red, White)        
    
    Red.move(1)
    Red.rotate(30)
    Red.rotate(30)
    Red.rotate(30)
    
    White.move(1)
    White.rotate(30)
    White.rotate(30)
    White.rotate(30)
    White.rotate(30)
    
    
    # Main game loop
    while not board.isGameOver():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit

        board.updateInfo()
        Red.fight()
        board.redraw() 

        board.updateInfo()
        White.fight()
        board.redraw() 
        
    
        # Detection of a hit.
        if (Tank.detectHit(Red, White)):
            board.addPointsTo(Red)
        elif Tank.detectHit(White, Red):
            board.addPointsTo(White)


        board.redraw()                
        board.slowDown()   