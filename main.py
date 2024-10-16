import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    print("Starting asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player1.draw(screen)
        player1.update(dt)

        pygame.display.flip()

        t = clock.tick(60)
        dt = t / 1000

if __name__ == "__main__":
    main()