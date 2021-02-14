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
pygame.display.set_caption('Coronavirus: Keep Your Distance')
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
player_width = 73
player_height = 73
clock = pygame.time.Clock()

# 3 - Load images
playerImg = pygame.image.load("/Users/Jocelyn/Downloads/main character (1).png")
coronaImg = pygame.image.load("/Users/Jocelyn/Downloads/Coronavirus .png")
secondcoronaImg = pygame.image.load("/Users/Jocelyn/Downloads/Second Coronavirus .png")
rightPlayer = pygame.image.load("/Users/Jocelyn/Downloads/Right Side Character.png")
leftPlayer = pygame.image.load("/Users/Jocelyn/Downloads/left side character.png")
backgroundImg = pygame.image.load("/Users/Jocelyn/Downloads/NEW Background.png")
startImg = pygame.image.load("/Users/Jocelyn/Downloads/New Piskel (2) 2 (1).jpg")


def player(x,y):
    gameDisplay.blit(playerImg, (x,y))

def coronavirus(x,y):
    gameDisplay.blit(coronaImg, (x,y))

def secondcoronavirus(x,y):
    gameDisplay.blit(secondcoronaImg, (x,y))

def rightplayer(x,y):
    gameDisplay.blit(rightPlayer, (x,y))

def leftplayer(x,y):
    gameDisplay.blit(leftPlayer, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',15)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

    
def crashVirus():
    message_display('481,000 Americans have passed away because of Covid. Take Covid seriously.')

def crashVirus2():
    message_display('108 million people have been infected by Covid. Take Covid seriously.')

def crashPerson():
    message_display('Make sure to social distance and keep 6 feet away at all times!')

def crashPerson2():
    message_display('Make sure to wear a mask and sanitize at all times!')


def game_loop(): 
    x =  (display_width * 0.45)
    y = (display_height * 0.45)
    x_change = 0
    y_change = 0
    player_speed = 0
    
    coronavirus_startx = random.randrange(0, display_width)
    coronavirus_starty = -1200
    secondcoronavirus_startx = random.randrange(0, display_width)
    secondcoronavirus_starty = 1500
    rightplayer_startx  = 2000
    rightplayer_starty = random.randrange(0, display_height)
    leftplayer_startx = -600
    leftplayer_starty = random.randrange(0, display_height)
    coronavirus_speed = 7
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            gameDisplay.blit(backgroundImg, [0,0])
            
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

        #gameDisplay.fill(white)
        gameDisplay.blit(backgroundImg, [0,0])
        coronavirus(coronavirus_startx, coronavirus_starty)
        coronavirus_starty += coronavirus_speed
        secondcoronavirus(secondcoronavirus_startx, secondcoronavirus_starty)
        secondcoronavirus_starty -= coronavirus_speed
        rightplayer(rightplayer_startx, rightplayer_starty)
        rightplayer_startx -= coronavirus_speed
        leftplayer(leftplayer_startx, leftplayer_starty)
        leftplayer_startx += coronavirus_speed
        player(x,y)
        #timer()
       

        if x > display_width - player_width or x < 0:
            x_change = 0

        if y > display_height - player_height or y < 0:
            y_change = 0

        if coronavirus_starty  > display_height:
                coronavirus_starty = 0 - coronavirus_height
                coronavirus_startx = random.randrange(0, display_width)

        if rightplayer_startx < 0:
                rightplayer_starty = random.randrange(0, display_width)
                rightplayer_startx = 900 + coronavirus_height

        if secondcoronavirus_starty  < 0:
                secondcoronavirus_starty = 800 + coronavirus_height
                secondcoronavirus_startx = random.randrange(0, display_width)

        if leftplayer_startx > display_width:
            leftplayer_starty = random.randrange(0, display_width)
            leftplayer_startx = 0 - coronavirus_height

                
        if y <= coronavirus_starty + coronavirus_height - 50 and y>= coronavirus_starty - coronavirus_height - 60:
            #('y crossover')

            if x >= coronavirus_startx and x<= coronavirus_startx + coronavirus_height - 40 or x + player_width >= coronavirus_startx  and x + player_width <= coronavirus_startx+ coronavirus_height - 40:
               # print('x crossover')
                crashVirus()
                #gameExit = True;
                
        if y <= secondcoronavirus_starty + coronavirus_height - 50 and y>= secondcoronavirus_starty - coronavirus_height - 60:
            #('y crossover')

            if x >= secondcoronavirus_startx and x<= secondcoronavirus_startx + coronavirus_height - 40 or x + player_width >= secondcoronavirus_startx  and x + player_width <= secondcoronavirus_startx+ coronavirus_height - 40:
               # print('x crossover')
                crashVirus2()
                #gameExit = True;

        if y <= rightplayer_starty + coronavirus_height - 50 and y>= rightplayer_starty - coronavirus_height - 60:
            #('y crossover')

            if x >= rightplayer_startx and x<= rightplayer_startx + coronavirus_height - 40 or x + player_width >= rightplayer_startx  and x + player_width <= rightplayer_startx+ coronavirus_height - 40:
               # print('x crossover')
                crashPerson()
                #gameExit = True;

        if y <= leftplayer_starty + coronavirus_height - 50 and y>= leftplayer_starty - coronavirus_height - 60:
            #('y crossover')

            if x >= leftplayer_startx and x<= leftplayer_startx + coronavirus_height - 40 or x + player_width >= leftplayer_startx  and x + player_width <= leftplayer_startx+ coronavirus_height - 40:
               # print('x crossover')
                crashPerson2()
                #gameExit = True;

        pygame.display.update()
        clock.tick(60)

black=(0,0,0)
end_it=False
while (end_it==False):
    gameDisplay.blit(startImg, [0,0])
    #nlabel=myfont.render("Welcome "+myname+" Start Screen", 1, (255, 0, 0))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            end_it=True
    #window.blit(nlabel,(200,200))
    pygame.display.flip()
game_loop()
pygame.quit()
quit()




