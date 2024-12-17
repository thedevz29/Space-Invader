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
    
#Bullet part
bullet_img = pygame.image.load()
bullet_x = 0
bullet_y = bullet_speed
bullet_state = "ready"

#Score part
score_value = 0
font = pygame.font.Font('Arial', 34)
text_x = 10
text_y = 10
over_font = pygame.font.Font('Arial', 64)

def show_score(x,y):
    
    score = font.render("Score: "+str(score_value),True(255,255,255))
    root.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,0))
    root.blit(over_text,(200,250))
    
def player(x,y):
    root.blit(player_img,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    root.blit(bullet_img,(x+16,y+10))

def isCollision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt((enemyx-bulletx)**2+(enemyy-bullety)**2)
    return distance<collision_distance


#Game loop
