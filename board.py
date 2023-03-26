from time import sleep
from math import atan, degrees
import pygame
import constants as const


class Board:
    def __init__(self, *tanks): 
        self.tank1, self.tank2 = tanks # tank1 = red, tank2 = white
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
        gameOver = self.points["total"] >= const.maxPointsToScore
        if gameOver: self.showGoodbyeMessage()
        return gameOver

    def showGoodbyeMessage(self):
        currMess = pygame.display.get_caption()[0]
        endMess = "** GAME OVER **"
        pygame.display.set_caption(f"{currMess} {endMess}")      

    def calcDistanceBetweenTanks(self):
        from math import dist
        if self.tank1 is None or self.tank2 is None: return 
            
        point1 = (self.tank1.x, self.tank1.y)
        point2 = (self.tank2.x, self.tank2.y)
        return dist(point1, point2)   
    
    def slowDown(self, seconds=0.5):
        sleep(seconds)

    def updateDistanceInfo(self):
        d = self.calcDistanceBetweenTanks()
        self.tank1.distToTarget = d
        self.tank2.distToTarget = d

    def updateAngleInfo(self):
        a = self.calcAngleToTarget()
        
        if a is not None:
            self.tank1.angleToTarget = a
            self.tank2.angleToTarget = -a
       
    def calcAngleToTarget(self):
        """Calculates the smallest angle (in degrees) that each tank needs to rotate in order to aim at the other tank."""
        if not self.tank1 or not self.tank2:
            return None
        x1, y1 = self.tank1.x, self.tank1.y
        x2, y2 = self.tank2.x, self.tank2.y
        angle = degrees(atan ((y1-y2) / (x1-x2))) + self.tank1.angle        
        normalized_angle = angle % 360
        normalized_angle -= 360 * (normalized_angle > 180)
        return normalized_angle
        
        
    def updateInfo(self):
        self.updateAngleInfo()
        self.updateDistanceInfo()       