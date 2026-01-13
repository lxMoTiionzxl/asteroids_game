from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        # unit_vector = pygame.Vector2(0, 1)
        # movement_vector_with_speed = unit_vector * self.velocity * dt
        movement_vector_with_speed = self.velocity * dt
        self.position += movement_vector_with_speed
