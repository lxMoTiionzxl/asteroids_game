from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import pygame
from pygame import display

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        # refreshes screen
        display.flip()

if __name__ == "__main__":
    main()
