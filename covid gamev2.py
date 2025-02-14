# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
display_width = 800
display_height = 600
gameDisplay=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PLACEHOLDER')
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
player_width = 73
player_height = 73
clock = pygame.time.Clock()

# 3 - Load images
playerImg = pygame.image.load("/Users/Jocelyn/Downloads/main character (1).png")

# 4 - keep looping through


def player(x,y):
    gameDisplay.blit(playerImg, (x,y))

def game_loop(): 
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    player_speed = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)
        player(x,y)

        if x > display_width - player_width or x < 0 or y > display_height - player_height or y < 0:
            gameExit = True
    
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()




