import pygame

pygame.init()
clock = pygame.time.Clock()
dt = 0

BETTER_BLUE = (52, 174, 235)

SCREEN = pygame.display.set_mode((1280, 760))
pygame.display.set_caption("Előre, utánam")

SCREEN.fill(BETTER_BLUE)
bilding = pygame.image.load("../images/bilding.png").convert_alpha()
ground = pygame.image.load("../images/ground.png").convert_alpha()
plane = pygame.image.load("../images/de.png").convert_alpha()

plane_position = (pygame.Vector2(100, 350))

SCREEN.blit(ground, (0, 600))
SCREEN.blit(ground, (500, 600))
SCREEN.blit(bilding, (500, 350))
SCREEN.blit(bilding, (600, 350))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.blit(plane, plane_position)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        plane_position.y -= 100 * dt
    if keys[pygame.K_a]:
        plane_position.x -= 100 * dt
    if keys[pygame.K_s]:
        plane_position.y += 100 * dt
    if keys[pygame.K_d]:
        plane_position.x += 100 * dt

    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()
