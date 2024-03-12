import pygame
import random

pygame.init()
clock = pygame.time.Clock()
dt = 0
GAME_ACTIVE = True


def spawn_explosion(x, y):
    pass


def shoot_missile():
    pass


BETTER_BLUE = (52, 174, 235)

SCREEN = pygame.display.set_mode((1280, 760))
pygame.display.set_caption("Előre, utánam")

game_font = pygame.font.SysFont('pressstart2pregular', 60)
game_overtext = game_font.render("GAME OVER", True, "white")
game_overtext_rect = game_overtext.get_rect(center=(SCREEN.get_width() / 2, SCREEN.get_height() / 2))

bilding = pygame.image.load("../images/bilding.png").convert_alpha()
bilding_rect = bilding.get_rect(midbottom=(SCREEN.get_width(), 550))

ground = pygame.transform.scale_by(pygame.image.load("../images/ground.png").convert_alpha(), 1.8)
ground_rect = ground.get_rect(bottomleft=(0, 850))
ground_rect2 = ground.get_rect(bottomleft=(SCREEN.get_width(), 850))

missiles = []

missile = pygame.image.load("../images/missile.png")

plane = pygame.image.load("../images/de.png").convert_alpha()

plane_rect = plane.get_rect(midbottom=(100, 300))

fighter = pygame.transform.scale_by(pygame.image.load("../images/fighter.png").convert_alpha(), 0.3)

fighter_rect = plane.get_rect(midbottom=(SCREEN.get_width(), 300))

counter = 0
explosion_index = 0
explosion = []
for i in range(0, 29):
    explosion.append(pygame.transform.scale_by(
        pygame.image.load(f'../images/fire_ball_side_medium/imgs_explode/img_{i}.png').convert_alpha(), 4))

blown = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if GAME_ACTIVE:
        if keys[pygame.K_w]:
            plane_rect.y -= 300 * dt
        if keys[pygame.K_a]:
            plane_rect.x -= 300 * dt
        if keys[pygame.K_s]:
            plane_rect.y += 300 * dt
        if keys[pygame.K_d]:
            plane_rect.x += 300 * dt
    else:
        if keys[pygame.K_SPACE]:
            GAME_ACTIVE = True
            bilding_rect.x = SCREEN.get_width()
            plane_rect = plane.get_rect(midbottom=(100, 300))
            fighter_rect = plane.get_rect(midbottom=(SCREEN.get_width(), 300))
            blown = False

    if GAME_ACTIVE:
        SCREEN.fill(BETTER_BLUE)
        SCREEN.blit(ground, ground_rect)
        SCREEN.blit(ground, ground_rect2)
        SCREEN.blit(bilding, bilding_rect)
        SCREEN.blit(plane, plane_rect)
        SCREEN.blit(fighter, fighter_rect)

        if plane_rect.x >= SCREEN.get_width():
            plane_rect.x = -100
        if ground_rect.x < -1280:
            ground_rect.x = SCREEN.get_width()
        if ground_rect2.x < -1280:
            ground_rect2.x = SCREEN.get_width()
        bilding_rect.x -= 400 * dt
        fighter_rect.x -= 850 * dt
        ground_rect.x -= 400 * dt
        ground_rect2.x -= 400 * dt

        if bilding_rect.x < -50:
            bilding_rect.x = SCREEN.get_width()
        if fighter_rect.x < -50:
            fighter_rect.x = SCREEN.get_width()
            fighter_rect.y = random.randint(0, 300)

        if plane_rect.colliderect(fighter_rect):
            GAME_ACTIVE = False
        if plane_rect.colliderect(bilding_rect):
            GAME_ACTIVE = False
    else:
        if not blown:
            counter += 1
            if counter % 7 == 0:
                explosion_index += 1
            if explosion_index > len(explosion) - 1:
                explosion_index = 0
                blown = True

            explosion_rect = explosion[explosion_index].get_rect(center=(fighter_rect.x, fighter_rect.y + 150))
            SCREEN.blit(explosion[explosion_index], explosion_rect)
        else:
            SCREEN.fill("red")
            SCREEN.blit(game_overtext, game_overtext_rect)


    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()
