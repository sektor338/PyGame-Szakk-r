import pygame

pygame.init()
clock = pygame.time.Clock()
dt = 0

BETTER_BLUE = (52, 174, 235)

SCREEN = pygame.display.set_mode((1280, 760))
pygame.display.set_caption("Előre, utánam")

bilding = pygame.image.load("../images/bilding.png").convert_alpha()
bilding_rect = bilding.get_rect(midbottom=(500, 600))

ground = pygame.transform.scale_by(pygame.image.load("../images/ground.png").convert_alpha(), 1.8)
ground_rect = ground.get_rect(bottomleft=(0, 760))


plane = pygame.image.load("../images/de.png").convert_alpha()

plane_rect = plane.get_rect(midbottom=(100, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print(clock.get_fps())

    SCREEN.fill(BETTER_BLUE)
    SCREEN.blit(ground, ground_rect)
    SCREEN.blit(bilding, bilding_rect)
    SCREEN.blit(plane, plane_rect)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        plane_rect.y -= 300 * dt
    if keys[pygame.K_a]:
        plane_rect.x -= 300 * dt
    if keys[pygame.K_s]:
        plane_rect.y += 300 * dt
    if keys[pygame.K_d]:
        plane_rect.x += 300 * dt

    if plane_rect.x >= SCREEN.get_width():
        plane_rect.x = -100

    if plane_rect.colliderect(bilding_rect):
        print("Ütközés 1")

    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()
