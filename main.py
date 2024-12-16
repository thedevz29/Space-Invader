import pygame 
import math 
import random

width, height = 800, 800
collision_distance = 20
x_change = 0
y_change = 0
player_start_x = 400
player_start_y = 700
enemy_start_y_min = 60
enemy_start_y_max = 170
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed = 30

pygame.init()
root = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("bg2.jpg")
bg_2 = pygame.transform.scale(bg)
#Player part
player_img = pygame.image.load("spaceship.png")
player_x = player_start_x
player_y = player_start_y
player_x_change = 0
#Enemy part
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_count = 7

for i in range(enemy_count):
    enemy_img.append("enemy.webp")
    enemy_x.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemy_y.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

bullet_img = pygame.image.load()
    