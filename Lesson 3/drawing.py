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
    # pygame.draw.rect(surface, (rgb szín), (x, y, a, b))
    # zöld felület
    pygame.draw.rect(SCREEN, (33, 219, 114), (0, 300, 800, 100))
    # bal gomba
    pygame.draw.rect(SCREEN, (255, 255, 255), (200, 200, 25, 100))
    # jobb gomba
    pygame.draw.rect(SCREEN, (255, 255, 255), (600, 200, 25, 100), 5, 10)
    # lábas gomba két lába
    pygame.draw.rect(SCREEN, (255, 255, 255), (450, 230, 15, 70), 2, 10)
    pygame.draw.rect(SCREEN, (255, 255, 255), (425, 230, 15, 70), 2, 10)

    # jobb oldali gomba tető
    pygame.draw.polygon(SCREEN, (255, 0, 0), [(583, 200), (612, 150), (640, 200)])

    # bal oldali gomba tető
    pygame.draw.polygon(SCREEN, (255, 0, 0), [(180, 200), (212, 150), (245, 200)])

    # középső gomba tető
    pygame.draw.polygon(SCREEN, (0, 0, 0), [(425, 230), (445, 180), (465, 230)])

    pygame.draw.ellipse(SCREEN, (255, 255, 255), (435, 220, 20, 5))

    pygame.draw.circle(SCREEN, (255, 255, 255), (440, 210), 3)
    pygame.draw.circle(SCREEN, (255, 255, 255), (450, 210), 3)

    pygame.draw.line(SCREEN, (252, 252, 35), (750, 50), (700, 50), 5)
    pygame.draw.line(SCREEN, (252, 252, 35), (750, 50), (750, 0), 5)
    pygame.draw.line(SCREEN, (252, 252, 35), (750, 50), (750, 100), 5)
    pygame.draw.line(SCREEN, (252, 252, 35), (750, 50), (800, 50), 5)

    pygame.draw.line(SCREEN, (252, 252, 35), (750, 50), (795, 10), 5)
    pygame.draw.line(SCREEN, (252, 252, 35), (750, 50), (790, 95), 5)
    pygame.draw.line(SCREEN, (252, 252, 35), (750, 50), (715, 95), 5)
    pygame.draw.line(SCREEN, (252, 252, 35), (750, 50), (715, 10), 5)

    # nap
    pygame.draw.circle(SCREEN, (252, 252, 35), (750, 50), 25)
    #nap szemei
    pygame.draw.circle(SCREEN, (0, 0, 0), (740, 45), 5)
    pygame.draw.circle(SCREEN, (0, 0, 0), (760, 45), 5)
    #nap szája
    pygame.draw.ellipse(SCREEN, (0, 0, 0), (740, 60, 20, 5))




    pygame.draw.ellipse(SCREEN, (255, 255, 255), (100, 50, 50, 20))
    pygame.draw.polygon(SCREEN, (237, 181, 14), [(145, 55), (160, 60), (145, 65)])  # sokszög
    pygame.draw.circle(SCREEN, (0, 0, 0), (140, 57), 2)
    pygame.draw.polygon(SCREEN, (220, 220, 220), [(110, 35), (120, 60), (130, 60)])  # sokszög

    pygame.display.update()

pygame.quit()
