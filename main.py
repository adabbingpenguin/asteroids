import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2, shots_group=shots_group)
    asteroid_field = AsteroidField()

    asteroids_to_split = []
    bullets_to_remove = []
    

    while True:
        pygame.Surface.fill(screen, "black")


        updatable.update(dt)
        shots_group.update(dt)


        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                print("Game over!")
                sys.exit()

            for bullet in shots_group:
                if asteroid.collides_with(bullet) == True:
                    asteroids_to_split.append(asteroid)
                    bullets_to_remove.append(bullet)

        for asteroid in asteroids_to_split:
            asteroid.split(asteroids)

        for bullet in bullets_to_remove:
            bullet.kill()

        asteroids_to_split = []
        bullets_to_remove = []

        for draw in drawable:
            draw.draw(screen)
        shots_group.draw(screen)    

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()