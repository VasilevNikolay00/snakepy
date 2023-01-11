import pygame, sys, random

class Fruit:
    def __init__(self):
        self.x = random.randint(0 , cell_number-1)
        self.y = random.randint(0 , cell_number-1)
        self.pos = pygame.Vector2(self.x,self.y)
        self.color = "Orange"

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,self.color,fruit_rect)

class Snake_body:
    def __init__(self):
        self.body  = [pygame.Vector2(5,10),pygame.Vector2(6,10),pygame.Vector2(7,10)]
        self.direction = pygame.Vector2(-1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,"Red", block_rect)


    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]

class Main:
    def __init__(self):
        self.snake = Snake_body()
        self.fruit = Fruit()    

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()

fruit = Fruit()
snake = Snake_body()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,150)

while True:

    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != pygame.Vector2(0,1):
                snake.direction = pygame.Vector2(0,-1)
            if event.key == pygame.K_DOWN and snake.direction != pygame.Vector2(0,-1):
                snake.direction = pygame.Vector2(0,1)
            if event.key == pygame.K_LEFT and snake.direction != pygame.Vector2(1,0):
                snake.direction = pygame.Vector2(-1,0)
            if event.key == pygame.K_RIGHT and snake.direction != pygame.Vector2(-1,0):
                snake.direction = pygame.Vector2(1,0)

        if event.type == screen_update:
            snake.move_snake()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("Dark Green")       
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)