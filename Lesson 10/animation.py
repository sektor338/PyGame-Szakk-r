import pygame
WIDTH, HEIGHT = 800, 400
BG_COLOR = (140, 137, 246)
BIRD_SPEED = 5
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bird_surf1 = pygame.image.load("../images/bird/bird1.png")
bird_surf2 = pygame.image.load("../images/bird/bird2.png")
bird_surf3 = pygame.image.load("../images/bird/bird3.png")
bird_surf4 = pygame.image.load("../images/bird/bird4.png")

bird_surf = [bird_surf1,bird_surf2,bird_surf3,bird_surf4]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BG_COLOR)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
