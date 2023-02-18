import pygame
from sys import exit


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(width/2, height))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += 2
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 2

    def shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bullets.add(Bullet(self.rect.midtop))

    def update(self):
        self.player_input()
        self.shoot()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.y -= 4


pygame.init()
win_size = width, height = 300, 500
screen = pygame.display.set_mode(win_size)
clock = pygame.time.Clock()
bg_color = "#00151c"

player = pygame.sprite.GroupSingle()
player.add(Player())
bullets = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(bg_color)

    player.draw(screen)
    player.update()

    bullets.draw(screen)
    bullets.update()

    pygame.display.update()
    clock.tick(60)
