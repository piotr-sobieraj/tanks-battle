import pygame, math
from time import sleep

class Tank:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.angle = 0
        self.draw_line = False


    def fight(self):
        self.rotate(-7)
        self.move_forward(-20)
    
    def rotate(self, angle_step):
        self.angle += angle_step

    def move_forward(self, distance):
        dx = distance * math.cos(math.radians(self.angle))
        dy = -distance * math.sin(math.radians(self.angle))
        self.move(dx, dy)
        
    
    def move(self, x, y):
        new_x = self.x + x
        new_y = self.y + y
        if 0 <= new_x - self.width / 2 <= window_width and 0 <= new_y - self.height / 2 <= window_height:
            self.x = new_x
            self.y = new_y
        
    def toggle_draw_line(self):
        self.draw_line = not self.draw_line
    
    
    def draw(self, surface):
        rect_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        rect_surface.fill((0, 0, 0, 0))
        pygame.draw.rect(rect_surface, self.color, (0, 0, self.width, self.height))
        rotated_surface = pygame.transform.rotate(rect_surface, self.angle)
        rect_rect = rotated_surface.get_rect()
        rect_rect.center = (self.x, self.y)
        surface.blit(rotated_surface, rect_rect)

        
        
import pygame

window_width = 500
window_height = 500
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Obracający się prostokąt")

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

tank = Tank(window_width/2, window_height/2, 20, 10, white)
rectangle1 = Tank(window_width/2, window_height/2, 20, 10, red)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     rectangle.rotate(-1)
    # if keys[pygame.K_RIGHT]:
    #     rectangle.rotate(1)
    # if keys[pygame.K_UP]:
    #     rectangle.move_forward(5)
    # if keys[pygame.K_DOWN]:
    #     rectangle.move_forward(-5)

    tank.rotate(5)
    tank.move_forward(10)

    rectangle1.fight()
    
            
    sleep(0.5)
    window.fill(black)
    tank.draw(window)
    rectangle1.draw(window)
    pygame.display.update()
