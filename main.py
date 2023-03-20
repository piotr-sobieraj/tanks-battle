import pygame
from time import sleep
from math import cos, sin, radians

# Definitions of colors for background and tanks
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

class Tank:
    def __init__(self, x, y, width, height, color):
        self.x = x # x coordinate of tank's center (center of gravity)
        self.y = y # y 
        self.width = width # width of the rectangle that represents tank
        self.height = height # height. Width should be > height (not checked)
        self.color = color 
        self.angle = 0 
        self.isAmmoReady = True 
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
        return 0 <= new_x - self.width / 2 <= window_width and 0 <= new_y - self.height / 2 <= window_height
    
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


# Window setup
window_width = 400
window_height = 400
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tanks battle")

# Initialisation of the tanks
redTank = Tank(window_width/2, window_height/2, 20, 10, red)
whiteTank = Tank(window_width/2, window_height/2, 20, 10, white)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
    
    # Tactics of the red tank - should be put in the fight method.
    redTank.rotate(5)
    redTank.move(10)

    # Tactics of the white tank - it should be always put in the fight method. 
    whiteTank.fight()

    # Detection of a hit.
    print(Tank.detectHit(redTank, whiteTank)) #shot fired by the white tank
    print(Tank.detectHit(whiteTank, redTank)) #shot fired by the red tank

    # Slows down the animation. 
    sleep(0.5)

    #Drawing / refreshing screen
    window.fill(green)
    redTank.draw(window)
    whiteTank.draw(window)
    pygame.display.update()    