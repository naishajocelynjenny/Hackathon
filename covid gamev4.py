# 1 - Import library
import pygame
import time
import random
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
display_width = 575
display_height = 575
coronavirus_height = 60
gameDisplay=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('ITS RAINING CORONA')
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
player_width = 73
player_height = 73
clock = pygame.time.Clock()

# 3 - Load images
playerImg = pygame.image.load("/Users/bharatiagarwal/Downloads/main character (1).png")
coronaImg = pygame.image.load("/Users/bharatiagarwal/Downloads/Coronavirus (1).png")

# 4 - keep looping through

def player(x,y):
    gameDisplay.blit(playerImg, (x,y))

def coronavirus(x,y):
    gameDisplay.blit(coronaImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
def crash():
    message_display('covid bad')

def game_loop(): 
    x =  (display_width * 0.45)
    y = (display_height * 0.45)
    x_change = 0
    y_change = 0
    player_speed = 0
    
    coronavirus_startx = random.randrange(0, display_width)
    coronavirus_starty = -600
    coronavirus_speed = 7
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -6
                elif event.key == pygame.K_RIGHT:
                    x_change = 6
                elif event.key == pygame.K_UP:
                    y_change = -6
                elif event.key == pygame.K_DOWN:
                    y_change = 6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0
                    

        x += x_change
        y += y_change

        gameDisplay.fill(white)
        coronavirus(coronavirus_startx, coronavirus_starty)
        coronavirus_starty += coronavirus_speed
        player(x,y)
       

        if x > display_width - player_width or x < 0:
            x_change = 0

        if y > display_height - player_height or y < 0:
            y_change = 0

        if coronavirus_starty  > display_height:
                coronavirus_starty = 0 - coronavirus_height
                coronavirus_startx = random.randrange(0, display_width)
        if y <= coronavirus_starty + coronavirus_height - 50 and y>= coronavirus_starty - coronavirus_height - 60 or y - player_height <= coronavirus_starty + coronavirus_height - 60 and y - player_height >= coronavirus_starty -coronavirus_height - 60:
            #('y crossover')

            if x >= coronavirus_startx and x<= coronavirus_startx + coronavirus_height - 40 or x + player_width >= coronavirus_startx  and x + player_width <= coronavirus_startx+ coronavirus_height - 40:
               # print('x crossover')
                crash()
                
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()




