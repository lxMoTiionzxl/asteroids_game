from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import pygame
from pygame import display
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot
import sys

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        # Other way of updating:
        updatable.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event('player_hit')
                print('Game over!')
                sys.exit()
            
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for item in drawable:
            item.draw(screen)

        # ===================== Last Lines Always ==========================
        # refreshes screen
        display.flip()
        # conversion delta time from ms to s
        dt = clock.tick(60) / 1000 


if __name__ == "__main__":
    main()
