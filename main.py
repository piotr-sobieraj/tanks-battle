from time import sleep
import pygame

import constants as const
from tank import Tank


pygame.init()
window = pygame.display.set_mode((const.windowWidth, const.windowHeight))
pygame.display.set_caption("Tanks battle")

# Create tanks
redTank = Tank(const.red)
whiteTank = Tank(const.white)

# Main game loop
while True:
    # Slows down the animation. 
    sleep(0.5)
    
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

    

    #Drawing / refreshing screen
    window.fill(const.green)
    redTank.draw(window)
    whiteTank.draw(window)
    pygame.display.update()    