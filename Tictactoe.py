import os
import pygame

pygame.init()

#CONSTANTS
DIM = 600
WIN = pygame.display.set_mode((DIM, DIM))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (200, 200, 200)
TILE_WIDTH = DIM / 3

#IMAGES
o_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "o.png")), (TILE_WIDTH - 5, TILE_WIDTH - 5))
x_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "x.png")), (TILE_WIDTH - 5, TILE_WIDTH - 5))

#CLASSES
class Board:
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def is_occupied(self, row, col):
        if self.board[row][col] != 0:
            return True
        return False

    def draw(self, WIN):
        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                if board.board[i][j] == "x":
                    WIN.blit(x_image, (j * TILE_WIDTH, i * TILE_WIDTH))
                elif board.board[i][j] == "o":
                    WIN.blit(o_image, (j * TILE_WIDTH, i * TILE_WIDTH))

    def is_winner(self):

        #Check rows for winner
        for row in board.board:
            if row in (["x", "x", "x"], ["o", "o", "o"]):
                return True

        #Check columns for winner
        for i in range(3):
            if board.board[0][i] == board.board[1][i] and board.board[0][i] == board.board[2][i]:
                if board.board[0][i] in ("x", "o"):
                    return True

        #Check diagonals for winner
        if board.board[0][0] == board.board[1][1] and board.board[0][0] == board.board[2][2]:
            if board.board[0][0] in ("x", "o"):
                return True
        if board.board[0][2] == board.board[1][1] and board.board[0][2] == board.board[2][0]:
            if board.board[0][2] in ("x", "o"):
                return True
        return False

class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_over(self, mouse_pos):
        if mouse_pos[0] >= self.x and mouse_pos[0] <= self.x + TILE_WIDTH:
            if mouse_pos[1] >= self.y and mouse_pos[1] <= self.y + TILE_WIDTH:
                return True
        return False

#OBJECTS
buttons = []
board = Board()

#FUNCTIONS
def draw(WIN, mouse_pos):
    WIN.fill(WHITE)
    draw_grid(WIN)
    tile_hover(WIN, mouse_pos)
    board.draw(WIN)

    pygame.display.update()

def draw_grid(WIN):
    x = 0
    y = 0
    checker = 1
    for i in range(3):
        for j in range(3):
            if checker==1:
                pygame.draw.rect(WIN, WHITE, (x, y, TILE_WIDTH, TILE_WIDTH))
            else:
                pygame.draw.rect(WIN, GREY, (x, y, TILE_WIDTH, TILE_WIDTH))
            if j != 3:
                checker*= -1
            x += TILE_WIDTH
        x = 0
        y += TILE_WIDTH

def handle_clicks(turn, mouse_pos):
    for button in buttons:
        if button.is_over(mouse_pos):
            col = int(button.x // TILE_WIDTH)
            row = int(button.y // TILE_WIDTH)
            if not board.is_occupied(row, col):
                if turn == "x":
                    board.board[row][col] = "x"
                    return "o"
                else:
                    board.board[row][col] = "o"
                    return "x"

def create_buttons():
    x = 0
    y = 0
    for i in range(3):
        for j in range(3):
            buttons.append(Button(x, y))
            x += TILE_WIDTH
        x = 0
        y += TILE_WIDTH

def tile_hover(WIN, mouse_pos):
    for button in buttons:
        if button.is_over(mouse_pos):
            pygame.draw.rect(WIN, RED, (button.x, button.y, TILE_WIDTH, TILE_WIDTH))

def main(WIN):

    create_buttons()

    run = True
    turn = "x"
    while run:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                result = handle_clicks(turn, mouse_pos)
                if result == "x":
                    turn = "x"
                elif result == "o":
                    turn = "o"
        draw(WIN, mouse_pos)
        if board.is_winner():
            run = False
        
main(WIN)

