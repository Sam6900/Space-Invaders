import pygame
from sys import exit
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(width/2, height))
        self.shoot_delay_ms = 1000
        self.last_shot_time = 0
        self.bullet_speed = -4

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
            bullets.add(Bullet(self.rect.midtop, self.bullet_speed))
            self.last_shot_time = current_time

    def update(self):
        self.player_input()
        self.shoot()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y < -10:
            self.kill()
            bullets.remove(self)
        elif self.rect.y > height + 10:
            self.kill()
            invader_bullets.remove(self)


class Invader(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.invader_speed = 1
        self.invader_jump_distance = 15
        self.invader_bullet_speed = 1
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

    def shoot(self):
        if randint(1, 800) == 7:
            invader_bullets.add(Bullet((self.rect.midbottom[0], self.rect.midbottom[1] + 16), self.invader_bullet_speed))

    def update(self):
        self.move()
        self.shoot()


def handle_collisions():
    if bool(bullets): pygame.sprite.groupcollide(bullets, invaders, True, True)
    if pygame.sprite.spritecollide(player.sprite, invaders, True):
        print("Game Over")
        return True
    return False


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

invader_bullets = pygame.sprite.Group()

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

    invaders.draw(screen)
    invaders.update()

    invader_bullets.draw(screen)
    invader_bullets.update()

    handle_collisions()
    pygame.display.update()
    dt = clock.tick(60)
