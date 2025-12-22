import pygame
from constants import *
from player import *
from logger import log_state

FPS = 60

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
      
    running = True 
    while running:
        log_state()
        dt = clock.tick(FPS) / 1000
        player_sprite = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")
        player_sprite.draw(screen)
        pygame.display.flip()
        

        
    pygame.quit()       

if __name__ == "__main__":
    main()
