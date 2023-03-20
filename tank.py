from math import cos, sin, radians
import constants as const
import pygame


class Tank:
    def __init__(self, color):
        self.x = const.windowWidth / 2 # x coordinate of tank's center 
        self.y = const.windowHeight / 2 # y
        self.width = const.tankWidth # width of the rectangle that represents tank
        self.height = const.tankHeight # height. Width should be > height (not forced)
        self.color = color 
        self.angle = 0 
        self.isAmmoReady = True # not implemented yet
        self.shotLine = tuple() # line that represents trajectory of the projectile
        self.rect = None # Rectangle that represents the tank

    def fight(self):
        """Nethod in which the gamer puts their tactics. Here can only be used: rotate and move. In future also: fire."""
        self.rotate(45)
        self.move(20)
    
    def rotate(self, angle):
        """Rotates the tank by angle degrees counterclockwise. Use negative number to rotate. """
        self.angle += angle

    def move(self, distance):
        """Moves the tank by distance pixels forward. Use negative number to move backward."""
        dx = distance * cos(radians(self.angle))
        dy = -distance * sin(radians(self.angle))
        self.moveTank(dx, dy)        
    
    def moveTank(self, x, y):
        """Calculates new coordinates of the tank and sets the new coords, if they fit within the board."""
        new_x = self.x + x
        new_y = self.y + y
        if self.isPointWithinBoard(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else: pass

    def isPointWithinBoard(self, new_x, new_y):
        """Checks whether new tank's coordinates would be within the board."""
        return 0 <= new_x - self.width / 2 <= const.windowWidth and 0 <= new_y - self.height / 2 <= const.windowHeight
    
    def getFrontCenter(self):
        """Calculates coordinates of the point lying on the front center of the tank - used to calculate trajectory of a projectile."""
        cx = self.x + (self.width / 2) * cos(radians(self.angle))
        cy = self.y - (self.width / 2) * sin(radians(self.angle))
        return cx, cy

    def drawTank(self, rect_surface):
        """Draws the shape of tank."""
        pygame.draw.rect(rect_surface, self.color, (0, 0, self.width, self.height))
    
    def draw(self, surface):
        """Draws the tank on given surface."""
        rect_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        rect_surface.fill((0, 0, 0, 0))
        self.drawTank(rect_surface)
        rotated_surface = pygame.transform.rotate(rect_surface, self.angle)
        self.rect = rotated_surface.get_rect()
        self.rect.center = (self.x, self.y)
        surface.blit(rotated_surface, self.rect)
        self.drawShoot(surface)

    def drawShoot(self, surface):
        """Draws a trajectowy of a projectile."""
        if self.isAmmoReady:
            front_center = self.getFrontCenter()

            # Obliczenie wektora kierunkowego 
            direction = (cos(radians(self.angle)), -sin(radians(self.angle)))
            
            # Obliczenie punktu końcowego linii
            end_point = (front_center[0] + 800 * direction[0], front_center[1] + 800 * direction[1])
            pygame.draw.line(surface, self.color, front_center, end_point, 1)
            self.shotLine = (front_center, end_point)

    @staticmethod
    def detectHit(hit, shooting):
        """Detects that hit tank was hit by the shooting tank."""
        if hit.rect is not None and shooting.shotLine is not None:
            return hit.rect.clipline(shooting.shotLine)