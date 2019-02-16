import pygame

WIDTH = 10
HEIGHT = 10
TIME_DELAY = 100 #ms

#colors (will be set by user)
red = 0
green = 0
blue = 0


print('\n---------------------------------')
print('\tWELCOME TO SNAKE!')
print('---------------------------------')

print('\nHow large would you like the game to be on your screen?\n')

#TODO: Input Validation
screen_x = int(input('Choose a number within (100-1500) for the width of the screen: '))
screen_y = int(input('Choose a number within (100-750) for the height of the screen: '))

#use these vars to set init loc of snake
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
velo = int(input('Please choose the speed of the game (5-20): '))

#initialize game object
pygame.init()

#set window size
win = pygame.display.set_mode((screen_x,screen_y))

#game title
pygame.display.set_caption('Snake')

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

    #reset background
    win.fill((0,0,0))

    #draw a cube
    pygame.draw.rect(win, (red, green, blue), (x_cube, y_cube, WIDTH, HEIGHT))
    pygame.display.update()

pygame.quit()
