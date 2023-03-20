from time import sleep
import pygame
import constants as const


class Board:
    def __init__(self, *tanks):
        self.tank1, self.tank2 = tanks        
        pygame.init()
        self.setWindowMode()
        self.setCaption("Tanks battle")

    def setWindowMode(self):
        self.window = pygame.display.set_mode((const.windowWidth, const.windowHeight))
    
    def redraw(self):
        self.window.fill(const.green)
        self.tank1.draw(self.window)
        self.tank2.draw(self.window)
        pygame.display.update()    

    def setCaption(self, text):
        pygame.display.set_caption(text)
    
    @staticmethod
    def slowDown(seconds=0.5):
        sleep(seconds)