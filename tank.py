from math import cos, sin, radians, sqrt, degrees, atan2
from numpy import sign
import constants as const
import pygame


class Tank:
    def __init__(self, color, x=const.windowWidth / 2, y=const.windowHeight / 2):
        self.x = x # x coordinate of tank's center 
        self.y = y # y
        self.width = const.tankWidth # width of the rectangle that represents tank
        self.length = const.tankLength # Length. Width should be > height (not forced)
        self.color = color 
        self.angle = 0 # angle to axe OX
        self.angleToTarget = None
        self.isAmmoReady = True # not implemented yet
        self.shotLine = tuple() # line that represents trajectory of the projectile
        self.rect = None # Rectangle that represents the tank

    def move(self, distance=const.tankLength):
        """Moves the tank by distance pixels forward. 
        Distance is cut down to length of the tank (10). 
        Use negative numbers to move backwards."""
        distance = max(distance, const.tankLength) * sign(distance)
        dx = distance * cos(radians(self.angle))
        dy = -distance * sin(radians(self.angle))
        self.moveTo(dx, dy)    

    def rotate(self, angle):
        """Rotates the tank by angle degrees counterclockwise. 
        Expects argument between -30 and 30. 
        Cuts down the argument so that if is always -30 to 30. 
        Use negative number to rotate clockwise."""
        s = sign(angle)
        angle = min(30, abs(angle))
        self.angle += s * angle
    
    def fightRed(self):
        """Nethod in which the gamer puts their tactics. 
        Here can only be used: rotate, move, distanceToOpponent and angleToOpponent """
        print(f"red to white = {self.angleToTarget}")
        self.move(10)      
        self.rotate(-5)

    def fightWhite(self):
        """Nethod in which the gamer puts their tactics. 
        Here can only be used: rotate, move, distanceToOpponent and angleToOpponent """
        # print(f"white to red = {self.angleToTarget}")
        

        
    def moveTo(self, x, y):
        """Calculates new coordinates of the tank and sets the new coords, 
        if they fit within the board."""
        new_x = self.x + x
        new_y = self.y + y
        if self.isPointWithinBoard(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else: pass

    def isPointWithinBoard(self, new_x, new_y):
        """Checks whether new tank's coordinates would be within the board."""
        return 0 <= new_x - self.width / 2 <= const.windowWidth and 0 <= new_y - self.length / 2 <= const.windowHeight
    
    def getFrontCenter(self):
        """Calculates coordinates of the point lying 
        on the front center of the tank - used to calculate 
        trajectory of a projectile."""
        cx = self.x + (self.width / 2) * cos(radians(self.angle))
        cy = self.y - (self.width / 2) * sin(radians(self.angle))
        return cx, cy

    def drawTank(self, rect_surface):
        """Draws the shape of tank."""
        pygame.draw.rect(rect_surface, self.color, (0, 0, self.width, self.length))
    
    def draw(self, surface):
        """Draws the tank on given surface."""
        rect_surface = pygame.Surface((self.width, self.length), pygame.SRCALPHA)
        rect_surface.fill((0, 0, 0, 0))
        self.drawTank(rect_surface)
        rotated_surface = pygame.transform.rotate(rect_surface, self.angle)
        self.rect = rotated_surface.get_rect()
        self.rect.center = (self.x, self.y)
        surface.blit(rotated_surface, self.rect)
        self.drawShoot(surface)

    def drawShoot(self, surface):
        """Draws a trajectowy of a projectile."""
        def diagonal(a, b):
            return sqrt(a**2 + b**2)
            
        if self.isAmmoReady:
            front_center = self.getFrontCenter()

            # Obliczenie wektora kierunkowego 
            direction = (cos(radians(self.angle)), -sin(radians(self.angle)))
            
            # Obliczenie punktu końcowego linii
            # Najdłuższa linia może być przekątną wymiarów boarda
            diag = diagonal(const.windowWidth, const.windowHeight)
            end_point = (front_center[0] + diag * direction[0], front_center[1] + diag * direction[1])
            pygame.draw.line(surface, self.color, front_center, end_point, width=1)
            self.shotLine = (front_center, end_point)


    @staticmethod
    def detectHit(hit, shooting):
        """Detects that the hit tank was hit by the shooting tank."""
        if hit.rect is not None and shooting.shotLine is not None:
            return hit.rect.clipline(shooting.shotLine)