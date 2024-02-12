import pygame


pygame.init()
clock = pygame.time.Clock()
dt = 0


GAME_ACTIVE = True

BETTER_BLUE = (52, 174, 235)

SCREEN = pygame.display.set_mode((1280, 760))
pygame.display.set_caption("Előre, utánam")

bilding = pygame.image.load("../images/bilding.png").convert_alpha()
bilding_rect = bilding.get_rect(midbottom=(1000, 600))
#bilding2 = pygame.image.load("../images/bilding.png").convert_alpha()
#bilding2_rect = bilding.get_rect(midbottom=(600, 600))

ground = pygame.image.load("../images/ground.png").convert_alpha()
plane = pygame.image.load("../images/de.png").convert_alpha()

plane_rect = plane.get_rect(midbottom=(100, 600))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if GAME_ACTIVE:
        SCREEN.fill(BETTER_BLUE)
        SCREEN.blit(ground, (0, 600))
        SCREEN.blit(ground, (500, 600))
        SCREEN.blit(bilding, bilding_rect)
        # SCREEN.blit(bilding2, bilding2_rect)
        SCREEN.blit(plane, plane_rect)
    else:
        SCREEN.fill("red")

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



    if plane_rect.x >= SCREEN.get_width():
        plane_rect.x = -100

    bilding_rect.x -= 200 * dt
    if bilding_rect.x < -20:
        bilding_rect.x = SCREEN.get_width()




    if plane_rect.colliderect(bilding_rect):
        GAME_ACTIVE = False

    #if plane_rect.colliderect(bilding2_rect):
        #print("Ütközés 2")


    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()