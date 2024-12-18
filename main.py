import pygame
import math
import random



# Constants
width, height = 800, 800
collision_distance = 20
player_start_x = 400
player_start_y = 600
enemy_start_y_min = 60
enemy_start_y_max = 170
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed = 30

# Initialize Pygame
pygame.init()
root = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("bg2.jpg")
bg2 = pygame.transform.scale(bg,(width,height))

# Player setup
player_img = pygame.image.load("spaceship.png")
player_x = player_start_x
player_y = player_start_y
player_x_change = 0

# Enemy setup
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_count = 7

for i in range(enemy_count):
    enemy_img.append(pygame.image.load("enemy.webp"))
    enemy_x.append(random.randint(0, width - 100))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

# Bullet setup
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = player_y
bullet_x_change = 0
bullet_y_change = bullet_speed
bullet_state = "ready"

# Score setup
score_value = 0
font = pygame.font.Font(None, 34)
text_x = 10
text_y = 10
over_font = pygame.font.Font(None, 64)

# Functions
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    root.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 0))
    root.blit(over_text, (200, 250))

def player(x, y):
    root.blit(player_img, (x, y))

def enemy(x, y, i):
    root.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    root.blit(bullet_img, (x + 16, y + 10))

def isCollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx - bulletx) ** 2 + (enemyy - bullety) ** 2)
    return distance < collision_distance

# Game loop
running = True
while running:
    root.fill((0, 0, 0))
    root.blit(bg2, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_x_change = 0

    # Update player position
    player_x += player_x_change
    player_x = max(0, min(player_x, width - 100))  # Prevent going out of bounds

    # Update enemies
    for i in range(enemy_count):
        if enemy_y[i] > 340:
            for j in range(enemy_count):
                enemy_y[j] = 2000
            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= width - 100:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]

        # Collision detection
        if isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = player_start_y
            bullet_state = "ready"
            score_value += 10
            enemy_x[i] = random.randint(0, width - 100)
            enemy_y[i] = random.randint(enemy_start_y_min, enemy_start_y_max)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = player_start_y
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()