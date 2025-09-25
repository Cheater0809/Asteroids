import ast
import sys
import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Container Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Assign containers to classes
    Player.containers = (updatable, drawable) # pyright: ignore[reportAttributeAccessIssue]
    Asteroid.containers = (asteroids, updatable, drawable) # pyright: ignore[reportAttributeAccessIssue]
    AsteroidField.containers = (updatable,) # pyright: ignore[reportAttributeAccessIssue]
    
    # Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # Game Loop
    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill screen
        screen.fill("black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
            
        # display update
        pygame.display.flip()
        
        # Collision detection
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over!")
                sys.exit(0)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
