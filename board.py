from time import sleep
import pygame
import constants as const


class Board:
    MAX_POINTS_TO_SCORE = 3 # Game ends after both players scored MAX_POINTS_TO_SCORE points
    def __init__(self, *tanks):
        self.tank1, self.tank2 = tanks      
        self.points = {x: 0 for x in tanks} | {"total": 0} 
        
        pygame.init()
        self.setWindowMode()
        self.setCaption("Welcome to Tanks Battle!")

    def setWindowMode(self):
        self.window = pygame.display.set_mode((const.windowWidth, const.windowHeight))
    
    def redraw(self):
        self.window.fill(const.green)        
        self.tank1.draw(self.window)
        self.tank2.draw(self.window)
        pygame.display.update()    

    def setCaption(self, text):
        pygame.display.set_caption(text)

    def addPointsTo(self, tank):
        self.points[tank] += 1      
        self.points["total"] += 1
        # Red is second
        t1 = self.tank1
        t2 = self.tank2
        self.setCaption(f"Red {self.points[t2]} : {self.points[t1]} White ")

    def isGameOver(self):
        gameOver = self.points["total"] >= Board.MAX_POINTS_TO_SCORE
        if gameOver: self.showGoodbyeMessage()
        return gameOver

    def showGoodbyeMessage(self):
        currMess = pygame.display.get_caption()[0]
        endMess = "** GAME OVER **"
        pygame.display.set_caption(f"{currMess} {endMess}")         

    @staticmethod
    def slowDown(seconds=0.5):
        sleep(seconds)