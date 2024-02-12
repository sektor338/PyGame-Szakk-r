import pygame

pygame.init()
clock = pygame.time.Clock()
dt = 0
GAME_ACTIVE = True
BETTER_BLUE = (52, 174, 235)

SCREEN = pygame.display.set_mode((1280, 760))
pygame.display.set_caption("Előre, utánam")


def spawn_tower():
    pass


# Text
print(pygame.font.get_fonts())
game_font = pygame.font.SysFont('hightowertext', 60)
gameover_text = game_font.render('GAME OVER', True, "white")
gameover_text_rect = gameover_text.get_rect(center=(SCREEN.get_width() / 2, SCREEN.get_height() / 2))

bird_surf_1 = pygame.image.load('../images/bird/bird1.png').convert_alpha()
bird_surf_2 = pygame.image.load('../images/bird/bird2.png').convert_alpha()
bird_surf_3 = pygame.image.load('../images/bird/bird3.png').convert_alpha()
bird_surf_4 = pygame.image.load('../images/bird/bird4.png').convert_alpha()
bird_surf = [bird_surf_1, bird_surf_2, bird_surf_3, bird_surf_4]
bird_index = 0
counter = 0
bird_rect = bird_surf[bird_index].get_rect(midleft=(0, SCREEN.get_height() / 2))

bilding = pygame.transform.scale_by(pygame.image.load("../images/bilding.png").convert_alpha(), 1.1)
bilding_rect = bilding.get_rect(midbottom=(600, 460))

# bilding2 = pygame.image.load("../images/bilding.png").convert_alpha()
# bilding_rect2 = bilding2.get_rect(midbottom=(600, 600))


# groundnak legyen rect +
ground = pygame.transform.scale_by(pygame.image.load("../images/ground.png").convert_alpha(), 1.8)
ground_rect = ground.get_rect(bottomleft=(0, 760))
plane = pygame.image.load("../images/de.png").convert_alpha()
plane_rect = plane.get_rect(center=(100, 350))

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
            plane = pygame.transform.flip(pygame.image.load("../images/de.png").convert_alpha(), True, False)
        if keys[pygame.K_s]:
            plane_rect.y += 300 * dt
        if keys[pygame.K_d]:
            plane_rect.x += 300 * dt
            plane = pygame.image.load("../images/de.png").convert_alpha()
    else:
        if keys[pygame.K_SPACE]:
            GAME_ACTIVE = True
            bilding_rect.x = SCREEN.get_width()
            plane_rect.x = 100

    if GAME_ACTIVE:
        SCREEN.fill(BETTER_BLUE)
        SCREEN.blit(ground, ground_rect)
        SCREEN.blit(bilding, bilding_rect)
        SCREEN.blit(plane, plane_rect)

        counter += 1
        if counter % 7 == 0:
            bird_index += 1
        if bird_index > len(bird_surf) - 1:
            bird_index = 0

        if bird_rect.x < SCREEN.get_width():
            bird_rect.x += 300 * dt
        SCREEN.blit(bird_surf[bird_index], bird_rect)

        if plane_rect.x >= SCREEN.get_width():
            plane_rect.x = -100
        bilding_rect.x -= 200 * dt

        if bilding_rect.x < -50:
            bilding_rect.x = SCREEN.get_width()

        if plane_rect.colliderect(bilding_rect):
            GAME_ACTIVE = False
    else:

        SCREEN.fill("red")
        SCREEN.blit(gameover_text, gameover_text_rect)

        '''
    if plane_rect.colliderect(bilding_rect2):
        print("robbanás 2")
'''
    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()
