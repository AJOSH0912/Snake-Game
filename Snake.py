import pygame
import time
import random
import os

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions
dis_width = 800
dis_height = 600

# Set up display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by [python]')

# Clock for controlling the game's frame rate
clock = pygame.time.Clock()

snake_block = 10
initial_snake_speed = 15

# Define font style
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Load high score
high_score_file = 'high_score.txt'
if os.path.exists(high_score_file):
    with open(high_score_file, 'r') as f:
        high_score = int(f.read())
else:
    high_score = 0

def save_high_score(high_score):
    with open(high_score_file, 'w') as f:
        f.write(str(high_score))

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, pos)

def show_score(score, high_score, lives, level):
    value = score_font.render(f"Score: {score}  High Score: {high_score}  Lives: {lives}  Level: {level}", True, yellow)
    dis.blit(value, [0, 0])

def game_over_screen(score, high_score):
    dis.fill(blue)
    message(f"Game Over! Your Score: {score}", red, [dis_width / 6, dis_height / 3])
    show_score(score, high_score, 0, 0)
    pygame.display.update()
    time.sleep(2)

def start_screen():
    dis.fill(blue)
    message("Welcome to Snake Game", yellow, [dis_width / 6, dis_height / 3])
    message("Press C to Play or Q to Quit", yellow, [dis_width / 6, dis_height / 2])
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    waiting = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
