import pygame

pygame.init()

SCREEN = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Első szakkör program")
SCREEN.fill((67, 199, 204))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #pygame.draw.rect(surface, (rgb szín), (x, y, a, b))
    #zöld felület
    pygame.draw.rect(SCREEN, (33, 219, 114), (0, 300, 800, 100))
    #bal gomba
    pygame.draw.rect(SCREEN, (255, 255, 255), (200, 200, 25, 100))
    #jobb gomba
    pygame.draw.rect(SCREEN, (255, 255, 255), (600, 200, 25, 100), 5, 10)
    #lábas gomba két lába
    pygame.draw.rect(SCREEN, (255, 255, 255), (450, 230, 15, 70), 2, 10)
    pygame.draw.rect(SCREEN, (255, 255, 255), (425, 230, 15, 70), 2, 10)


    #jobb oldali gomba tető
    pygame.draw.polygon(SCREEN, (255, 0, 0), [(583, 200), (612, 150), (640, 200)])

    #bal oldali gomba tető
    pygame.draw.polygon(SCREEN, (255, 0, 0), [(180, 200), (212, 150), (245, 200)])



    pygame.display.update()

pygame.quit()
