import pygame

pygame.init()

SCREEN = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Karácsonyi képeslap")

carpet = pygame.image.load("../images/christmas/carpet.png").convert_alpha()
carpet = pygame.transform.scale(carpet, (300, 200))


running = True
SCREEN.fill("white")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    SCREEN.blit(carpet, (250, 200))

pygame.quit()
