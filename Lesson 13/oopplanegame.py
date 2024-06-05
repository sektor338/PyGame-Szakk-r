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


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../images/de.png").convert_alpha()
        self.rect = self.image.get_rect()

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

player = Player()
all_sprites_list.add(player)


def display_score():
    score_surf = game_font.render("Score: " + str(score), True, "red")
    score_rect = score_surf.get_rect(topleft=(10, 10))
    SCREEN.blit(score_surf, score_rect)


game_overtext = game_font.render("GAME OVER", True, "white")
game_overtext_rect = game_overtext.get_rect(center=(SCREEN.get_width() / 2, SCREEN.get_height() / 2))


explosion_sfx = pygame.mixer.Sound("../sounds/explosion.mp3")
bg_music = pygame.mixer.Sound("../sounds/fallingskies.mp3")


bilding = pygame.image.load("../images/bilding.png").convert_alpha()
bilding_rect = bilding.get_rect(midbottom=(SCREEN.get_width(), 550))

ground = pygame.transform.scale_by(pygame.image.load("../images/ground.png").convert_alpha(), 1.8)
ground_rect = ground.get_rect(bottomleft=(0, 850))
ground_rect2 = ground.get_rect(bottomleft=(SCREEN.get_width() - 18, 850))
print(ground.get_width())

plane = pygame.image.load("../images/de.png").convert_alpha()

plane_rect = plane.get_rect(midbottom=(100, 300))

fighter = pygame.transform.scale_by(pygame.image.load("../images/fighter.png").convert_alpha(), 0.3)

fighter_rect = plane.get_rect(midbottom=(SCREEN.get_width(), 300))

score = 0
bg_music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if GAME_ACTIVE:
        all_sprites_list.update()
    else:
        if keys[pygame.K_SPACE]:
            GAME_ACTIVE = True
            bg_music.play()
            score = 0
            bilding_rect.x = SCREEN.get_width()
            plane_rect = plane.get_rect(midbottom=(100, 300))
            fighter_rect = plane.get_rect(midbottom=(SCREEN.get_width(), 300))
        elif keys[pygame.K_q]:
            running = False
    if GAME_ACTIVE:
        SCREEN.fill(BETTER_BLUE)
        SCREEN.blit(ground, ground_rect)
        SCREEN.blit(ground, ground_rect2)
        SCREEN.blit(bilding, bilding_rect)
        all_sprites_list.draw(SCREEN)
        SCREEN.blit(fighter, fighter_rect)
        display_score()



        if plane_rect.x >= SCREEN.get_width():
            plane_rect.x = -100

        bilding_rect.x -= 400 * dt
        ground_rect.x -= 400 * dt
        ground_rect2.x -= 400 * dt
        fighter_rect.x -= 650 * dt

        if ground_rect.x < -1280:
            ground_rect.x = SCREEN.get_width()
        if ground_rect2.x < -1280:
            ground_rect2.x = SCREEN.get_width()

        if bilding_rect.x < -50:
            score += 1
            bilding_rect.x = SCREEN.get_width()
        if fighter_rect.x < -50:
            score += 1
            fighter_rect.x = SCREEN.get_width()
            fighter_rect.y = random.randint(0, 300)

        if player.rect.colliderect(fighter_rect):
            explosion_sfx.play()
            GAME_ACTIVE = False
        if player.rect.colliderect(bilding_rect):
            explosion_sfx.play()
            GAME_ACTIVE = False
        if player.rect.colliderect(ground_rect):
            explosion_sfx.play()
            GAME_ACTIVE = False
        if player.rect.colliderect(ground_rect2):
            explosion_sfx.play()
            GAME_ACTIVE = False
    else:
        bg_music.stop()
        SCREEN.fill("red")
        SCREEN.blit(game_overtext, game_overtext_rect)

    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()
