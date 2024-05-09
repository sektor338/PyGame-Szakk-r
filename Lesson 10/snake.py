import pygame
import random

pygame.init()

CLR_BLACK = (0, 0, 0)
CLR_GREEN = (0, 255, 0)
CLR_RED = (255, 0, 0)

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600

display = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
pygame.display.set_caption("Snake Pygame")

clock = pygame.time.Clock()

SNAKE_BLOCK_SIZE = 10
SNAKE_SPEED = 15

FONT_STYLE = pygame.font.SysFont("pressstart2pregular", 30)


def display_score(score):
    score_text = FONT_STYLE.render("Score: " + str(score), True, CLR_RED)
    display.blit(score_text, [0, 0])


def draw_snake(snake_block_size, snake_body):
    for block in snake_body:
        pygame.draw.rect(display, CLR_GREEN, [block[0], block[1], snake_block_size, snake_block_size])


def display_message(msg, color):
    message = FONT_STYLE.render(msg, True, color)
    message_rect = message.get_rect(center=(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))
    display.blit(message, message_rect)


def game_loop():
    game_over = False
    game_close = False
    snake_x = DISPLAY_WIDTH / 2
    snake_y = DISPLAY_HEIGHT / 2

    snake_x_change = 0
    snake_y_change = 0

    snake_body = []
    snake_length = 1

    food_x = round(random.randrange(0, DISPLAY_WIDTH - SNAKE_BLOCK_SIZE) / 10) * 10
    food_y = round(random.randrange(0, DISPLAY_HEIGHT - SNAKE_BLOCK_SIZE) / 10) * 10

    while not game_over:
        while game_close:
            display.fill(CLR_BLACK)
            display_message("You lost press R or Q", CLR_RED)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -SNAKE_BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = SNAKE_BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_x_change = 0
                    snake_y_change = -SNAKE_BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    snake_x_change = 0
                    snake_y_change = SNAKE_BLOCK_SIZE

        if snake_x >= DISPLAY_WIDTH or snake_x < 0 or snake_y >= DISPLAY_HEIGHT or snake_y < 0:
            game_close = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        display.fill(CLR_BLACK)

        pygame.draw.rect(display, CLR_RED, [food_x, food_y, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK_SIZE, snake_body)
        display_score(snake_length - 1)
        pygame.display.update()
        if snake_x == food_x and snake_y == food_y:
            snake_length += 1
            food_x = round(random.randrange(0, DISPLAY_WIDTH - SNAKE_BLOCK_SIZE) / 10) * 10
            food_y = round(random.randrange(0, DISPLAY_HEIGHT - SNAKE_BLOCK_SIZE) / 10) * 10
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


game_loop()
