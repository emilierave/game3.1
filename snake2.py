import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 30)

# Set up the snake
snake_block_size = 10
snake_speed = 15
snake_list = []
snake_length = 1
snake_x = window_width / 2
snake_y = window_height / 2

# Set up the food
food_block_size = 10
food_x = round(random.randrange(
    0, window_width - food_block_size) / 10.0) * 10.0
food_y = round(random.randrange(
    0, window_height - food_block_size) / 10.0) * 10.0

# Set up the game loop
game_over = False
clock = pygame.time.Clock()

# Define a function to display the snake on the screen


def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(
            window, black, [x[0], x[1], snake_block_size, snake_block_size])


# Set up the main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= snake_block_size
    if keys[pygame.K_RIGHT]:
        snake_x += snake_block_size
    if keys[pygame.K_UP]:
        snake_y -= snake_block_size
    if keys[pygame.K_DOWN]:
        snake_y += snake_block_size

    # Check if the snake has collided with the wall
    if snake_x < 0 or snake_x > window_width - snake_block_size or snake_y < 0 or snake_y > window_height - snake_block_size:
        game_over = True

    # Check if the snake has collided with itself
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    # Check if the snake has eaten the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(
            0, window_width - food_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(
            0, window_height - food_block_size) / 10.0) * 10.0
        snake_length += 1

    # Draw the game screen
    window.fill(white)
    pygame.draw.rect(
        window, red, [food_x, food_y, food_block_size, food_block_size])
    draw_snake(snake_block_size, snake_list)
    score = font.render("Score: " + str(snake_length - 1), True, black)
    window.blit(score, [0, 0])
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# End the game
pygame.quit()
quit()
