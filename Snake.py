import random
import pygame

game_run = True

#display variables
height_display = 1000
width_display = 1000
#display setup
pygame.init()
dis=pygame.display.set_mode((width_display,height_display))
pygame.display.set_caption("Zmiq bace")
pygame.display.update()
clock = pygame.time.Clock()

#colors
blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)

#character position
char_X = width_display/2
char_Y = height_display/2
change_X = 0
change_Y = 0
speed = 3


#fruit stuff
x_fruit = 100
y_fruit = 100
fruit_eaten = True

def wall_collision():

    collsion_check = False

    if char_X > width_display-50 or char_X < 0 or char_Y > height_display-50 or char_Y < 0:
        collsion_check = True

    return collsion_check

def object_collision(x_obj,y_obj):
    collsion_check = False

    if char_X == x_obj or char_Y == y_obj:
        collsion_check = True

    return collsion_check

   

#gameloop
while game_run == True:
    #wall collision
    if wall_collision() == True:
        game_run = False

    if object_collision(x_fruit, y_fruit) == True:
        fruit_eaten = True

    for event in pygame.event.get():

        #closure event
        if event.type == pygame.QUIT:
            game_run = False

       

        #key input event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_X = - 50
                change_Y = 0

            if event.key == pygame.K_RIGHT:
                change_X = 50
                change_Y = 0

            if event.key == pygame.K_UP:
                change_Y = - 50
                change_X = 0
                

            if event.key == pygame.K_DOWN:
                change_Y = 50
                change_X = 0
                
        
        if fruit_eaten == True:
            print("qdene")
            x_fruit = random.randrange(width_display+50-(width_display%50),0,50)

            y_fruit = random.randrange(height_display+50-(height_display%50),0,50)

            fruit_eaten = False


    char_X += change_X 
    char_Y += change_Y
    
  
    pygame.draw.rect(dis, red,[x_fruit,y_fruit,50,50])
    pygame.draw.rect(dis, blue,[char_X,char_Y,50,50])
    pygame.display.update()
    dis.fill(black)
    clock.tick(speed)

#closing the game process
pygame.quit()
quit()

