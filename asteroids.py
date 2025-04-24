import pygame
import random
from circleshape import *
from constants import *



class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius,  width=2)
    
    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self, asteroids):

    
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        random_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create new asteroids with the correct constructor arguments
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        
        # Set velocity after creation
        new_asteroid_1.velocity = new_vector1 * 10
        new_asteroid_2.velocity = new_vector2 * 10

        asteroids.add(new_asteroid_1, new_asteroid_2)
        self.kill()

