import math

from snake import Snake
from point import Point
from input_test import read_input
from direction import Direction

width = 30
height = 20

starting_coord = (math.ceil(width/2), math.ceil(height/2))
snake = Snake(starting_coord) # The snake should start in the middle of the board
point = Point(width, height)
score = 0

def draw_board():
    board = [['⬜'] * width for _ in range(height)]
    board[point.y][point.x] = '⬛'
    for x, y in snake.coordinates:
        board[y][x] = '🟩'

    for row in board:
        print(''.join(row))

def clear_terminal():
    # ANSI escape codes: move the cursor to the top-left (\033[H)
    # and clear the screen (\033[2J).
    # Works on Linux/maxOS and windows.
    print('\033[H\033[2J', end='', flush=True)

# Arrow keys send ESC [ A-D. Some terminals send ESC O A-D instead.
ansi_to_direction = {
    '\033[A': Direction.UP,
    '\033[B': Direction.DOWN,
    '\033[C': Direction.RIGHT,
    '\033[D': Direction.LEFT,
    '\033OA': Direction.UP,
    '\033OB': Direction.DOWN,
    '\033OC': Direction.RIGHT,
    '\033OD': Direction.LEFT,
}

def out_of_bounds(coord):
    return (coord[0] >= width) or (coord[0] < 0) or (coord[1] >= height) or (coord[1] < 0)

def draw(board_x, board_y, character):
    # Translate game_board coordinates to terminal coordinates based on 2 things:
    # 1) Terminal uses 1 based indexing, while the board uses 0 based indexing
    # 2) Each emoji is 2 columns wide
    # Also, make sure the cursor goes back to the row that's after the board
    terminal_x = (2 * board_x) + 1
    terminal_y = board_y + 1
    print(f'\033[{terminal_y};{terminal_x}H{character}\033[{height+1};1H', flush=True, end='')


# game loop:
def game_loop():
    draw_board()
    while True:
        user_input = read_input()
        new_direction = ansi_to_direction[user_input]

        # ignore if direction is opposite of current direction
        if snake.direction and snake.direction.is_opposite(new_direction):
            clear_terminal()
            continue

        # Get the coordinates of the next location
        x_offset, y_offset = new_direction.value
        head_x, head_y = snake.coordinates[-1]
        new_head_x, new_head_y = (head_x + x_offset, head_y + y_offset)

        # Check if out of bounds or if the snake ran into itself (the current implementation of this is inefficient)
        if out_of_bounds((new_head_x, new_head_y)) or (new_head_x, new_head_y) in snake.coordinates:  
            # TODO
            break

        # Check if snake has eaten the point
        if new_head_x == point.x and new_head_y == point.y:
            snake.expand(new_direction)
            draw(new_head_x, new_head_y, '🟩')
            point.generate_new_coordinate()
            draw(point.x, point.y, '⬛')

        else:
            prev_tail_x, prev_tail_y = snake.coordinates[0]
            snake.move(new_direction)
            
            draw(prev_tail_x, prev_tail_y, '⬜')
            draw(new_head_x, new_head_y, '🟩')

        #clear_terminal()

try:
    # enter alternate screen and disable mouse scrolling
    # also, make sure the cursor is at row 1 column 1 in the terminal so that
    # there is no space above the game board
    print('\033[?1049h\033[?1000h\033[1:1H', end='', flush=True)
    game_loop()
finally:
    # always make sure to exit alternate screen
    print('\033[?1049l\033[?]', end='', flush=True)

'''
Scenarios where we need to replace characters in the board:

1) Snake moves (replace tail with background, replace new coordinate with head)
2) Snake eats dot: no need to replace tail, replace dot with snake, replace a random tile with dot

# Maybe have a map called squares_to_update that maps coordinates with the new emoji that needs to be placed there
# and / or have a function called update that takes a coordinate and an emoji and replaces that coordinate with that emoji

'''