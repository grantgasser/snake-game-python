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

#colors for the scoring
box_color = (0,0,0)
text_color = (64,224,208)

#to store coordinates of all cubes in the snake
x_coords = []
y_coords = []

#for shift
temp_x_list = []
temp_y_list = []

#to append new cube at end of lists
last_x = 0
last_y = 0

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

# get size of screen, color, and speed of game
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
    velo = int(input('Please choose the speed of the game (10-15): '))
    while velo < 10:
        print('Pick it up, you are going too slow!')
        velo = int(input('Please choose the speed of the game (10-15): '))

    while  velo > 15:
        print('Slow down, do you want a ticket?')
        velo = int(input('Please choose the speed of the game (5-15): '))

    return screen_x, screen_y, color, velo

def get_score():
    #create the box
    box = pygame.draw.rect(win, box_color, ((screen_x/3), (screen_y/2.5), (screen_x/2), (screen_y/5)))
    #sets the font
    font = pygame.font.SysFont("comicsansms", 35)
    #writes the text
    text = font.render("YOUR SCORE: " + str(score), True, text_color)
    #outputs the text
    win.blit(text,(box))
    #redraws the screen
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()


#get user input
screen_x, screen_y, color, velo = get_input()

#head is first coordinate, start in middle of screen
x_coords.append(screen_x/2)
y_coords.append(screen_y/2)

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

#draw snack initially
def draw_snack():
    pygame.draw.rect(win, (snack_red, snack_green, snack_blue), (snack_x, snack_y, CUBE_WIDTH, CUBE_HEIGHT))
    pygame.display.update()

draw_snack()

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

    #save prev head location and set new one
    prev_head_x = x_coords[0]
    prev_head_y = y_coords[0]
    x_coords[0] += velo_x
    y_coords[0] += velo_y

    #DETERMINE IF LOSE HERE
    # Set boundaries, lose if go off screen
    if x_coords[0] < 0 or x_coords[0] > screen_x or y_coords[0] < 0 or y_coords[0] > screen_y:
        run = False


    #if run into self
    i = 3
    assert(len(x_coords) == len(y_coords))
    while i < len(x_coords):
        if(x_coords[0] == x_coords[i] and y_coords[0] == y_coords[i]):
            run = False
        i += 1


    #if snake eats snack
    if(abs(snack_x-x_coords[0]) <= MARGIN and abs(snack_y-y_coords[0]) <= MARGIN) and run:
        snack_x = random.randint(1, screen_x)
        snack_y = random.randint(1, screen_y)

        x_coords.append(last_x)
        y_coords.append(last_y)

        score += 1


    #reset background
    win.fill((0,0,0,0))

    #shift values of cubes so that each cube follows the one before it
    temp_x_list.clear()
    temp_y_list.clear()
    i = 1

    assert(len(x_coords) == len(y_coords))
    while i < len(x_coords) and run:
        if i == 1:
            temp_x_list.append(x_coords[i])
            temp_y_list.append(y_coords[i])
            x_coords[i] = prev_head_x
            y_coords[i] = prev_head_y

        else:
            temp_x_list.append(x_coords[i])
            temp_y_list.append(y_coords[i])
            x_coords[i] = temp_x_list[i-2]
            y_coords[i] = temp_y_list[i-2]

        i += 1


    #draw all snake cubes
    i = 0

    assert(len(x_coords) == len(y_coords))
    while i < len(x_coords) and run:
        pygame.draw.rect(win, (red, green, blue), (x_coords[i], y_coords[i], CUBE_WIDTH, CUBE_HEIGHT))
        pygame.display.update()
        i += 1

    #draw snack
    if run:
        draw_snack()

        last_x = x_coords[len(x_coords)-1]
        last_y = y_coords[len(y_coords)-1]

#displays the score
print('\nThanks for playing!\n')
get_score()
