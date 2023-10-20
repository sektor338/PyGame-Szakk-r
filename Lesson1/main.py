import pygame

pygame.init()

SCREEN = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Első szakkör program")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()