import pygame
from sys import exit


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect()


pygame.init()
win_size = width, height = 300, 500
screen = pygame.display.set_mode(win_size)
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle()
player.add(Player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.draw(screen)
    player.update()

    pygame.display.update()
    clock.tick(60)
