import pygame
import random
import math

CUBE_WIDTH = 10
CUBE_HEIGHT = 10
TIME_DELAY = 100 #ms
MARGIN = 10

#colors
red = 0
green = 0
blue = 0

#screen size and speed of snake
screen_x = 0
screen_y = 0
velo = 0
velo_x = 0
velo_y = 0

#other
color = ''
curr_direction = '' #so as to not go backwards
score = 0

#snack cube, make snack yellow
snack_x = 0
snack_y = 0
snack_red = 255
snack_green = 255
snack_blue = 0

# function(get-input)
def get_input():
    correct_color = False

    print('\n---------------------------------')
    print('\tWELCOME TO SNAKE!')
    print('---------------------------------')

    print('\nHow large would you like the game to be on your screen?\n')

    #Get screen size from user
    screen_x = int(input('Choose a number within (500-1500) for the width of the screen: '))
    while screen_x < 500 or screen_x > 1500:
        print('Invalid input value!')
        screen_x = int(input('Choose a number within (500-1500) for the width of the screen: '))

    screen_y = int(input('Choose a number within (500-750) for the height of the screen: '))
    while screen_y < 500 or screen_y > 750:
        print('Invalid input value!')
        screen_y = int(input('Choose a number within (500-750) for the height of the screen: '))

    #Get color from user
    print('\nIt is time to choose your snake color (we recommend green!)')
    while not correct_color:
        color = input("Press 'r' for red, 'g' for green, and 'b' for blue: ")
        color = color.lower()

        if color == 'r':
            correct_color = True
        elif color == 'g':
            correct_color = True
        elif color == 'b':
            correct_color = True

    #Get speed from user
    velo = int(input('Please choose the speed of the game (5-15): '))
    while velo < 5:
        print('Pick it up, you are going too slow!')
        velo = int(input('Please choose the speed of the game (5-15): '))

    while  velo > 15:
        print('Slow down, do you want a ticket?')
        velo = int(input('Please choose the speed of the game (5-15): '))

    return screen_x, screen_y, color, velo

#get user input
screen_x, screen_y, color, velo = get_input()

#use these vars to set init loc of snake (center of screen)
x_cube = screen_x / 2
y_cube = screen_y / 2

#set colors
if(color == 'r'):
    red = 255
elif(color == 'g'):
    green = 255
elif(color == 'b'):
    blue = 255

#initialize game object
pygame.init()

#set window size
win = pygame.display.set_mode((screen_x,screen_y))

#game title
pygame.display.set_caption('Snake')

#randomly place snack
snack_x = random.randint(MARGIN, screen_x-MARGIN)
snack_y = random.randint(MARGIN, screen_y-MARGIN)

#draw snake
pygame.draw.rect(win, (snack_red, snack_green, snack_blue), (snack_x, snack_y, CUBE_WIDTH, CUBE_HEIGHT))
pygame.display.update()

run = True

#run game, much of this code comes from PyGame documentation
while run:

    pygame.time.delay(TIME_DELAY)

    #event is click or mouse move, returns list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #get key input from user
    key = pygame.key.get_pressed()

    #move in key direction
    if event.type == pygame.KEYDOWN:
        if key[pygame.K_LEFT] and curr_direction != 'r':
            velo_x = - velo
            velo_y = 0
            curr_direction = 'l'
        if key[pygame.K_RIGHT] and curr_direction != 'l':
            velo_x = velo
            velo_y = 0
            curr_direction = 'r'
        if key[pygame.K_UP] and curr_direction != 'd':
            velo_y = - velo
            velo_x = 0
            curr_direction = 'u'
        if key[pygame.K_DOWN] and curr_direction != 'u':
            velo_y = velo
            velo_x = 0
            curr_direction = 'd'

        #remember last direction, can't go backwards in snake
        last_key = key

    x_cube = x_cube + velo_x
    y_cube = y_cube + velo_y


    #if snake eats snack
    if(abs(snack_x-x_cube) <= 10 and abs(snack_y-y_cube) <= 10):
        snack_x = random.randint(1, screen_x)
        snack_y = random.randint(1, screen_y)
        score += 1

    # Set boundaries
    if x_cube < 0 or x_cube > screen_x or y_cube < 0 or y_cube > screen_y:
        run = False

    #reset background
    win.fill((0,0,0))

    #redraw snake and redraw snack
    pygame.draw.rect(win, (red, green, blue), (x_cube, y_cube, CUBE_WIDTH, CUBE_HEIGHT))
    pygame.draw.rect(win, (snack_red, snack_green, snack_blue), (snack_x, snack_y, CUBE_WIDTH, CUBE_HEIGHT))
    pygame.display.update()

print("Score:", score)

pygame.quit()
