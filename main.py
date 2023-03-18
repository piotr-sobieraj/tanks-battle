import pygame
from time import sleep
from math import cos, sin, radians

class Tank:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.angle = 0
        self.isAmmoReady = True   
        self.line = tuple()
        self.rect = None

    def fight(self):
        self.rotate(-7)
        self.move_forward(-20)
    
    def rotate(self, angle_step):
        self.angle += angle_step

    def move_forward(self, distance):
        dx = distance * cos(radians(self.angle))
        dy = -distance * sin(radians(self.angle))
        self.move(dx, dy)        
    
    def move(self, x, y):
        new_x = self.x + x
        new_y = self.y + y
        if self.isPointWithinBoard(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else: pass

    def isPointWithinBoard(self, new_x, new_y):
        return 0 <= new_x - self.width / 2 <= window_width and 0 <= new_y - self.height / 2 <= window_height

    
    def toggleAmmoReady(self):
        self.isAmmoReady = not self.isAmmoReady


    def get_front_center(self):
        cx = self.x + (self.width / 2) * cos(radians(self.angle))
        cy = self.y - (self.width / 2) * sin(radians(self.angle))
        return cx, cy

    def drawTank(self, rect_surface):
        pygame.draw.rect(rect_surface, self.color, (0, 0, self.width, self.height))
    
    def draw(self, surface):
        rect_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        rect_surface.fill((0, 0, 0, 0))
        self.drawTank(rect_surface)
        rotated_surface = pygame.transform.rotate(rect_surface, self.angle)
        rect_rect = rotated_surface.get_rect()

        self.rect = rect_rect
        
        rect_rect.center = (self.x, self.y)
        surface.blit(rotated_surface, rect_rect)
        self.drawShoot(surface)

    def drawShoot(self, surface):
        if self.isAmmoReady:
            front_center = self.get_front_center()

            # Obliczenie wektora kierunkowego 
            direction = (cos(radians(self.angle)), -sin(radians(self.angle)))
            
            # Obliczenie punktu końcowego linii
            end_point = (front_center[0] + 800 * direction[0], front_center[1] + 800 * direction[1])
            pygame.draw.line(surface, self.color, front_center, end_point, 1)
            self.line = (front_center, end_point)

    @staticmethod
    def detectHit(tank1, tank2):
        if tank1.rect is not None and tank2.line is not None:
            return tank1.rect.clipline(tank2.line)

    
            
        
        
        
window_width = 500
window_height = 500
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tanks battle")

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

redTank = Tank(window_width/2, window_height/2, 20, 10, red)
whiteTank = Tank(window_width/2, window_height/2, 20, 10, white)

# whiteTank.rotate(90)
# whiteTank.move_forward(100)
# whiteTank.rotate(-90)
# whiteTank.move_forward(100)
# whiteTank.rotate(-90)



licznik = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit

    redTank.rotate(5)
    redTank.move_forward(10)
    
    whiteTank.fight()

    # print(whiteTank.rect)
    print(Tank.detectHit(redTank, whiteTank)) #strzal białego
    print(Tank.detectHit(whiteTank, redTank)) #strzal czerwonego
    
    # print(f"{redTank.rect=}", 
    #       f"{whiteTank.line=}", 
    #       sep="\t")
            
    window.fill(black)
    redTank.draw(window)

    sleep(0.21)
        
    whiteTank.draw(window)
    licznik += 1
    pygame.display.update()
    
