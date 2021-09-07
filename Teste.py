import pygame
import os
import random
pygame.font.init()

from pygame import draw

pygame.display.set_caption("Primeiro")

# aqui jaz constantes
WIDTH, HEIGTH = 900, 500
POWER_UP_WIDTH, POWER_UP_HEIGTH = 30, 30
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 69, 0)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 44
VEL = 10
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("assets", "spaceship_yellow.png")
)
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    90,
)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    270,
)

HEART_IMAGE = pygame.image.load(os.path.join("assets", "Heart.png"))
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGTH))
BORDER = pygame.Rect(WIDTH // 2 - 10, 0, 10, HEIGTH)
BULLET_VEL = 15
MAX_BULLETS = 300
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
POWER_UP_YELLOW = pygame.USEREVENT + 3
POWER_UP_RED = pygame.USEREVENT + 4

POWER_UP = pygame.Rect(-100, -100, POWER_UP_WIDTH, POWER_UP_HEIGTH)

def yellow_handle_movement(keys_pressed, yellow):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # DIREITA
        yellow.x -= VEL
    if (
        keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x
    ):  # ESQUERDA
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # CIMA
        yellow.y -= VEL
    if (
        keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGTH - 5
    ):  # BAIXO
        yellow.y += VEL
    global POWER_UP
    if yellow.colliderect(POWER_UP):
        POWER_UP = pygame.Rect(-100, -100, POWER_UP_WIDTH, POWER_UP_HEIGTH)
        pygame.event.post(pygame.event.Event(POWER_UP_YELLOW))
    

def red_handle_movement(keys_pressed, red):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # DIREITA
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # ESQUERDA
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # CIMA
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGTH - 5:  # BAIXO
        red.y += VEL
    global POWER_UP
    if red.colliderect(POWER_UP):
        POWER_UP = pygame.Rect(-100, -100, POWER_UP_WIDTH, POWER_UP_HEIGTH)
        pygame.event.post(pygame.event.Event(POWER_UP_RED))
    


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_window(red, yellow, red_bullets, yellow_bullets, yellow_health, red_health):
    WIN.blit(SPACE, (0, 0))
    
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    red_health_text = HEALTH_FONT.render("health " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("health " + str(yellow_health), 1, WHITE)
    
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    global POWER_UP
    if POWER_UP.x <=0 :
        POWER_UP.x, POWER_UP.y = random.randint(0, WIDTH - POWER_UP_WIDTH), random.randint(0, HEIGTH - POWER_UP_HEIGTH)
        
    WIN.blit(HEART_IMAGE, (POWER_UP.x, POWER_UP.y))    
    
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGTH//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(1000)


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    power_up_num = []
    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width,
                        yellow.y + yellow.height // 2 - 2,
                        10,
                        5,
                    )
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_SPACE and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    
            if event.type == RED_HIT:
                red_health -= 1
                
            if event.type == POWER_UP_RED:
                red_health += 1
                
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                
            if event.type == POWER_UP_YELLOW:
                yellow_health += 1
                
            winner_text = ""    
            
            
            if yellow_health <= 0:
                winner_text = "Red win!" 
                
            if red_health <= 0:
                winner_text = "yellow win!"
            
            if winner_text != "":
                draw_winner(winner_text)
                main()
                
                
        keys_pressed = pygame.key.get_pressed()
        red_handle_movement(keys_pressed, red)
        yellow_handle_movement(keys_pressed, yellow)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, yellow_health, red_health)
    




if __name__ == "__main__":
    main()
