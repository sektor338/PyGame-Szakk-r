import pygame
import random

pygame.init()
clock = pygame.time.Clock()
dt = 0
GAME_ACTIVE = True

BETTER_BLUE = (52, 174, 235)

SCREEN = pygame.display.set_mode((1280, 760))
pygame.display.set_caption("Előre, utánam")
game_font = pygame.font.SysFont('pressstart2pregular', 60)


class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("../images/fighter.png").convert_alpha(), 0.3)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN.get_width() + 50

    def update(self):
        self.rect.x -= 650 * dt
        if self.rect.x < -50:
            self.rect.x = SCREEN.get_width() + 50
            self.rect.y = random.randint(0, 300)


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.flip(pygame.transform.scale_by(pygame.image.load("../images/missile.png").convert_alpha(), 0.5), True, False)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 800 * dt


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("../images/playerjet.png").convert_alpha(), 0.15)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def update(self):
        keyss = pygame.key.get_pressed()
        if keyss[pygame.K_w]:
            if self.rect.y >= 0:
                self.rect.y -= 300 * dt
        if keyss[pygame.K_a]:
            if self.rect.x >= 0:
                self.rect.x -= 300 * dt
        if keyss[pygame.K_s]:
            self.rect.y += 300 * dt
        if keyss[pygame.K_d]:
            if self.rect.x != SCREEN.get_width():
                self.rect.x += 300 * dt



all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

player = Player()
all_sprites_list.add(player)

enemy = EnemyPlane()
all_sprites_list.add(enemy)
enemy_list.add(enemy)


def display_score():
    score_surf = game_font.render("Score: " + str(score), True, "red")
    score_rect = score_surf.get_rect(topleft=(10, 10))
    SCREEN.blit(score_surf, score_rect)


game_overtext = game_font.render("GAME OVER", True, "white")
game_overtext_rect = game_overtext.get_rect(center=(SCREEN.get_width() / 2, SCREEN.get_height() / 2))

explosion_sfx = pygame.mixer.Sound("../sounds/explosion.mp3")
bg_music = pygame.mixer.Sound("../sounds/dangerzone.mp3")

bilding = pygame.image.load("../images/bilding.png").convert_alpha()
bilding_rect = bilding.get_rect(midbottom=(SCREEN.get_width(), 550))

ground = pygame.transform.scale_by(pygame.image.load("../images/ground.png").convert_alpha(), 1.8)
ground_rect = ground.get_rect(bottomleft=(0, 850))
ground_rect2 = ground.get_rect(bottomleft=(SCREEN.get_width() - 18, 850))
print(ground.get_width())

score = 0
bg_music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
    keys = pygame.key.get_pressed()

    if GAME_ACTIVE:
        all_sprites_list.update()
    else:
        if keys[pygame.K_SPACE]:
            GAME_ACTIVE = True
            bg_music.play()
            score = 0
            bilding_rect.x = SCREEN.get_width()
        elif keys[pygame.K_q]:
            running = False
    if GAME_ACTIVE:
        SCREEN.fill(BETTER_BLUE)
        SCREEN.blit(ground, ground_rect)
        SCREEN.blit(ground, ground_rect2)
        SCREEN.blit(bilding, bilding_rect)

        for bullet in bullet_list:
            block_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)

            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1
                print(score)

            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)


        all_sprites_list.draw(SCREEN)
        display_score()

        bilding_rect.x -= 400 * dt
        ground_rect.x -= 400 * dt
        ground_rect2.x -= 400 * dt

        if ground_rect.x < -1280:
            ground_rect.x = SCREEN.get_width()
        if ground_rect2.x < -1280:
            ground_rect2.x = SCREEN.get_width()

        if bilding_rect.x < -50:
            score += 1
            bilding_rect.x = SCREEN.get_width()

        if player.rect.colliderect(bilding_rect):
            explosion_sfx.play()
            GAME_ACTIVE = False
        if player.rect.colliderect(ground_rect):
            explosion_sfx.play()
            GAME_ACTIVE = False
        if player.rect.colliderect(ground_rect2):
            explosion_sfx.play()
            GAME_ACTIVE = False
        if player.rect.colliderect(enemy):
            explosion_sfx.play()
            GAME_ACTIVE = False
    else:
        bg_music.stop()
        SCREEN.fill("red")
        SCREEN.blit(game_overtext, game_overtext_rect)

    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()
