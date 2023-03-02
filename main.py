import pygame
from sys import exit
from datetime import datetime


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(width/2, height))
        self.shoot_delay_ms = 1000
        self.last_shot_time = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += 2
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 2

    def shoot(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and current_time - self.last_shot_time > self.shoot_delay_ms:
            bullets.add(Bullet(self.rect.midtop))
            self.last_shot_time = current_time


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
        if self.rect.y < -10:
            self.kill()
            bullets.remove(self)


class Invader(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.invader_speed = 2
        self.invader_jump_distance = 30
        self.posx = posx
        self.move_right = True
        self.image = pygame.image.load("assets/invader.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(posx, posy))

    def move(self):
        if self.move_right and self.rect.x < self.posx + width / 3:
            self.rect.x += self.invader_speed
        elif not self.move_right and self.rect.x > self.posx:
            self.rect.x -= self.invader_speed
        else:
            self.rect.y += self.invader_jump_distance
            self.move_right = not self.move_right

    def update(self):
        self.move()


def bullet_colllisions():
    if bool(bullets): pygame.sprite.groupcollide(bullets, invaders, True, True)


pygame.init()
win_size = width, height = 300, 500
screen = pygame.display.set_mode(win_size)
clock = pygame.time.Clock()
bg_color = "#00151c"

player = pygame.sprite.GroupSingle()
player.add(Player())
bullets = pygame.sprite.Group()

invaders = pygame.sprite.Group()
invaders_spacing = 30
for i in range(6):
    invaders.add(Invader((i * invaders_spacing) + 10, 30))

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
    bullet_colllisions()

    invaders.draw(screen)
    invaders.update()

    pygame.display.update()
    dt = clock.tick(60)
