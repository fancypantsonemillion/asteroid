import pygame 
from logger import log_state
from constants import *
from player import *

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    clock = pygame.time.Clock()
    dt = 0

    #CREATE groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #CREATE containers
    Player.containers = (updatable, drawable)

    #CREATE objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    #START game loop
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #UPDATE phase
        updatable.update(dt)
        
        #DRAW phase
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
         
        pygame.display.flip()

        #TICK phase
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
