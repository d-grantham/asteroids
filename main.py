import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for _ in asteroids:
            if _.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for _ in drawable:
            _.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()
