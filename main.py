import pygame
from sys import exit

pygame.init()
win_size = width, height = 300, 500
screen = pygame.display.set_mode(win_size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
