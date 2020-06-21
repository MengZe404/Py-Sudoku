'''
Py-Sudoku, version 1.0

A classic puzzle game made with PyGame!

(C) MengZe 2020-present
'''

# Copyright information.
__author__ = 'MengZe'
__copyright__ = '(C) MengZe 2020-present'
__license__ = 'Public Domain'
__version__ = '1.0.0'

# Libraries
############################
import pygame
import numpy as np
import csv
import random
import time

# Initialisation
pygame.init()

square_length = 60

screen_width = square_length * 9 + 300
screen_height = square_length * 9

font = pygame.font.Font('freesansbold.ttf', 28)
title_font = pygame.font.Font('freesansbold.ttf', 38)
sub_font = pygame.font.Font('freesansbold.ttf', 14)

# Game asset, downloaded from - https://www.pinterest.com/pin/153263193544481131/
table = pygame.image.load("table.jpg")

# Create square object that can be selected once at a time by the user
class Square(object):
    def __init__(self,win, x, y, coor):
        self.win = win
        self.x = x
        self.y = y
        self.coor = coor
        self.select = False
        # Position the square at the right spot (ignore this line <3)
        pygame.draw.rect(self.win, (255,255,255), (square_length * self.x + 4, square_length * self.y + 4, square_length - 8, square_length - 8))

    def selected(self):
        pygame.draw.rect(self.win, (220, 220, 220), (square_length * self.x + 4, square_length * self.y + 4, square_length - 8, square_length - 8))
        self.select = True

# Create number (text) objects that display on the game interface
class Number(object):
    def __init__(self, win, num, x, y, color):
        self.win = win
        self.num = num
        self.x = x
        self.y = y
        self.text = None
        self.color = color
        self.text = font.render('{}'.format(num), True, color)

    def draw(self):  
        self.win.blit(self.text, (square_length * self.x + 20, square_length * self.y + 20))

grid = np.empty(shape = [9,9], dtype = Square)

# Load the template stored in .txt file
file_template = open("template.txt", 'r')
reader1 = csv.reader(file_template)
template = [row for row in reader1]

file_answer = open("answer.txt", 'r')
reader2 = csv.reader(file_answer)
answer = [row for row in reader2]

# Backend

number_grid = []
answer_grid = []

# The game template is loaded to number_grid and whenever the user enter a number, it updates
# When number_grid == answer_grid, the puzzle is done
def generate(): 
    global number_grid
    global answer_grid
    global number

    number = np.empty(shape = [9,9], dtype = Number)

    number_grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    answer_grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    puzzle_index = random.randint(0, 5)

    # Generate the puzzle
    for row in range(9 * puzzle_index, 9 * puzzle_index + 9):
        number_grid[row - 9 * puzzle_index] = template[row][0].split(' ')
        answer_grid[row - 9 * puzzle_index] = answer[row][0].split(' ')

# Uptdae the grid
def update(win, num, row, col, color = (0,0,0)):
    if num == '0':
        pass
    else:
        number_grid[row][col] = num
        number[row][col] = Number(win, num, col, row, color)
        grid[row][col] = Square(win, col, row, (row, col))

# The main game
def main():
    global grid
    global number_grid

    generate()

    clock = pygame.time.Clock()

    # Screen config
    win = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sudoku")

    win.fill((255,255,255))
    win.blit(table, (0,0))

    title = title_font.render("Py-Sudoku", True, (0,0,0))
    subtitle = sub_font.render("~ Made by MengZe", True, (0,0,0))
    intro_1 = sub_font.render("# Select the box by clicking on it.", True, (0,0,0))
    intro_2 = sub_font.render("# Fill in the number using number keys", True, (0,0,0))

    win.blit(title, (square_length * 9 + 50, 50))
    win.blit(subtitle, (square_length * 9 + 100, 100))
    win.blit(intro_1, (square_length * 9 + 20, 160))
    win.blit(intro_2, (square_length * 9 + 20, 200))

    # Draw all the squares and numbers
    for row in range(0, 9):
        for col in range(0, 9):
            grid[row][col] = Square(win, col, row, (row, col))
            update(win, number_grid[row][col], row, col, (0,0,255))
                              
#### Main loop
    run = True
    while run:
        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                for row in range(0, 9):
                    for col in  range(0, 9):
                        if x in range((grid[row][col].x * square_length + 4), (grid[row][col].x * square_length + 57)) and y in range((grid[row][col].y * square_length + 4), (grid[row][col].y * square_length + 57)):
                            grid[row][col].selected()
                        else:
                            grid[row][col] = Square(win, col, row, (row, col))


        keys = pygame.key.get_pressed()
        
        # When the puzzle is done, do this:
        if number_grid == answer_grid:
            congrats = font.render("Congratulations!", True, (255,0,0))
            new = sub_font.render("Press 'n' key to start a new game!", False, (255,0,0))
            win.blit(congrats, (square_length * 9 + 35, 300))
            win.blit(new, (square_length * 9 + 30, 350))
            if keys[pygame.K_n]:
                generate()
                main()
                for row in range(0, 9):
                    for col in range(0, 9):
                        grid[row][col] = Square(win, col, row, (row, col))
                        update(win, number_grid[row][col], row, col, color=(0,0,255))

        for row in range(0, 9):
            for col in range(0, 9):
                if number[row][col] != None:
                    number[row][col].draw()
                # This allows the user in enter number
                if grid[row][col].select:
                    if keys[pygame.K_1]:
                        update(win, 1, row, col)
                    elif keys[pygame.K_2]:
                        update(win, 2, row, col)
                    elif keys[pygame.K_3]:
                        update(win, 3, row, col)
                    elif keys[pygame.K_4]:
                        update(win, 4, row, col)
                    elif keys[pygame.K_5]:
                        update(win, 5, row, col)
                    elif keys[pygame.K_6]:
                        update(win, 6, row, col)
                    elif keys[pygame.K_7]:
                        update(win, 7, row, col)
                    elif keys[pygame.K_8]:
                        update(win, 8, row, col)
                    elif keys[pygame.K_9]:
                        update(win, 9, row, col)
                    elif keys[pygame.K_0] or keys[pygame.K_ESCAPE]:
                        update(win, '', row, col) 
                           
        # Display everything
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

