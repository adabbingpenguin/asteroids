import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        
        # Create a larger, more visible shot
        self.image = pygame.Surface((SHOT_RADIUS*2, SHOT_RADIUS*2), pygame.SRCALPHA)
        # Fill circle instead of just outlining it
        pygame.draw.circle(self.image, (255, 0, 0), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
        
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        self.position = self.position + self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))