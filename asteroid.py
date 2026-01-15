from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        movement_vector_with_speed = self.velocity * dt
        self.position += movement_vector_with_speed

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        split_angle = uniform(20,50)
        new_asteroid_velocity = self.velocity.rotate(split_angle)
        new_opposing_asteroid_velocity = -self.velocity.rotate(split_angle)
        self.radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid = Asteroid(self.position[0], self.position[1], self.radius)
        new_opposing_asteroid = Asteroid(self.position[0], self.position[1], self.radius)

        new_asteroid.velocity = new_asteroid_velocity * 1.2
        new_opposing_asteroid.velocity = new_opposing_asteroid_velocity * 1.2