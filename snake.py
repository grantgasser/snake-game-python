import pygame
import random
import math

cube_width = 10
cube_height = 10
TIME_DELAY = 100 #ms

#colors (will be set by user)
red = 0
green = 0
blue = 0

#snack cube, make snack yellow
snack_x = 0
snack_y = 0
snack_red = 255
snack_green = 255
snack_blue = 0


print('\n---------------------------------')
print('\tWELCOME TO SNAKE!')
print('---------------------------------')

print('\nHow large would you like the game to be on your screen?\n')

#TODO: Input Validation
screen_x = int(input('Choose a number within (500-1500) for the width of the screen: '))
screen_y = int(input('Choose a number within (500-750) for the height of the screen: '))

#use these vars to set init loc of snake (center of screen)
x_cube = screen_x / 2
y_cube = screen_y / 2

#can draw circles for eyes
#x_eyes =
#y_eyes =


#TODO: Input Validation
print('\nIt is time to choose your snake color (we recommend green!)')
color = input("Press 'r' for red, 'g' for green, and 'b' for blue: ")
color = color.lower()

#set colors
if(color == 'r'):
    red = 255
elif(color == 'g'):
    green = 255
elif(color == 'b'):
    blue = 255

#TODO: Input Validation
velo = int(input('Please choose the speed of the game (5-15): '))

#initialize game object
pygame.init()

#set window size
win = pygame.display.set_mode((screen_x,screen_y))

#game title
pygame.display.set_caption('Snake')

#randomly place snack
snack_x = random.randint(1, screen_x)
snack_y = random.randint(1, screen_y)

pygame.draw.rect(win, (snack_red, snack_green, snack_blue), (snack_x, snack_y, cube_width, cube_height))
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
    keys = pygame.key.get_pressed()

    #move
    if keys[pygame.K_LEFT]:
        x_cube -= velo
    if keys[pygame.K_RIGHT]:
        x_cube += velo
    if keys[pygame.K_UP]:
        y_cube -= velo
    if keys[pygame.K_DOWN]:
        y_cube += velo


    #if snake eats snack
    if(abs(snack_x-x_cube) <= 10 and abs(snack_y-y_cube) <= 10):
        snack_x = random.randint(1, screen_x)
        snack_y = random.randint(1, screen_y)

    #reset background
    win.fill((0,0,0))

    #draw snake and redraw snack
    pygame.draw.rect(win, (red, green, blue), (x_cube, y_cube, cube_width, cube_height))
    pygame.draw.rect(win, (snack_red, snack_green, snack_blue), (snack_x, snack_y, cube_width, cube_height))
    pygame.display.update()

pygame.quit()
