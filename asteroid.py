import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) # pyright: ignore[reportArgumentType]
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        velo1 = self.velocity.rotate (angle)
        velo2 = self.velocity.rotate (-angle)
        rad1 = self.radius - ASTEROID_MIN_RADIUS
        rad2 = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, rad1) # type: ignore
        asteroit2 = Asteroid(self.position.x, self.position.y, rad2) # type: ignore
        asteroid1.velocity = velo1 * 1.2
        asteroit2.velocity = velo2 * 1.2