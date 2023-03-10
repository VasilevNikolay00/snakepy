import random
import sys

import pygame


class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.Vector2(self.x, self.y)
        self.color = "Orange"

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, self.color, fruit_rect)

    def randomise(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.Vector2(self.x, self.y)


class SnakeBody:
    def __init__(self):
        self.body = [pygame.Vector2(2, 3), pygame.Vector2(3, 3)]
        self.direction = [-1, 0]
        self.current_direction = self.direction
        self.newBlock = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if block == self.body[0]:
                pygame.draw.rect(screen, "Black", block_rect)
            else:
                pygame.draw.rect(screen, "Red", block_rect)

    def move_snake(self):
        if (self.body[0] + self.direction) != self.body[1]:
            self.current_direction = self.direction

        if self.newBlock:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.current_direction)
            self.body = body_copy[:]
            self.newBlock = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.current_direction)
            self.body = body_copy[:]

    def add_bodyblock(self):
        self.newBlock = True


class Main:
    def __init__(self):
        self.snake = SnakeBody()
        self.fruit = Fruit()
        self.GameOver = False

    def update(self):
        self.snake.move_snake()
        self.fruit_collision()
        self.fail_check()

    def draw_elements(self):

        self.snake.draw_snake()

        for block in self.snake.body:
            if self.fruit.pos == block:
                self.fruit.randomise()

        self.fruit.draw_fruit()

    def fruit_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomise()
            self.snake.add_bodyblock()

    def fail_check(self):
        for block in self.snake.body[1:]:
            if self.snake.body[0] == block:
                self.GameOver = True
                print("Self eat")

        if not 0 <= self.snake.body[0].x < cell_number:
            self.GameOver = True
            print("Wall X")

        if not 0 <= self.snake.body[0].y < cell_number:
            self.GameOver = True
            print("Wall Y")

    def illegal_movecheck(self, new_direct):

        if self.body[0] + new_direct:
            return False

        return True


pygame.init()
cell_size = 20
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

main_game = Main()

while True:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = [0, -1]
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = [0, 1]
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = [-1, 0]
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = [1, 0]
            if event.key == pygame.K_p:
                pygame.time.set_timer(screen_update, 0)
            if event.key == pygame.K_o:
                pygame.time.set_timer(screen_update, 150)

        if event.type == screen_update:
            main_game.update()

        if event.type == pygame.QUIT or main_game.GameOver:
            pygame.quit()
            sys.exit()

    screen.fill("Dark Green")
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
