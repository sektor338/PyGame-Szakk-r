import pygame
import random


class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill("green")
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill("red")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()

for i in range(50):
    block = Block("blue")
    block.rect.x = random.randrange(SCREEN_WIDTH)
    block.rect.y = random.randrange(340)
    block_list.add(block)
    all_sprites_list.add(block)

player = Player()
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()
score = 0
player.rect.y = 370

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    all_sprites_list.update()

    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)

        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    SCREEN.fill("white")
    all_sprites_list.draw(SCREEN)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()