from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import pygame
from pygame import display
from player import Player

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        # Other way of updating:
        updatable.update(dt)
        # drawable.draw(screen)

        # for item in updateable:
        #     item.update(dt)

        for item in drawable:
            item.draw(screen)


        # ===================== Last Lines Always ==========================
        # refreshes screen
        display.flip()
        # conversion delta time from ms to s
        dt = clock.tick(60) / 1000 


if __name__ == "__main__":
    main()
