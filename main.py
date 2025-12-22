import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from logger import log_state

FPS = 60

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
      
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable) 
    player_sprite = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()  
    
    running = True
    while running:
        log_state()
        dt = clock.tick(FPS) / 1000
        updatable.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        

        
    pygame.quit()       

if __name__ == "__main__":
    main()
