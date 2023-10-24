import pygame

pygame.init()

SCREEN = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Első szakkör program")

leftEye = pygame.Surface((100, 100))
leftIris = pygame.Surface((50, 50))
leftIris.fill("white")

rightEye = pygame.Surface((100, 100))
rightIris = pygame.Surface((50, 50))
rightIris.fill("white")


mouth = pygame.Surface((400, 50))
mouth.fill("green")

running = True
SCREEN.fill("wheat")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    SCREEN.blit(leftEye, (150, 50))
    SCREEN.blit(rightEye, (550, 50))
    SCREEN.blit(mouth, (200, 300))

    leftEye.blit(leftIris, (50, 50))
    rightEye.blit(rightIris, (0, 50))

    pygame.display.update()

    # korlátozás 60 FPS-re
    # 1 fps > 10px/s * 1 fps > 10px/s
    # 100 fps > 10px/s * 100 fps > 1000px/s

pygame.quit()
