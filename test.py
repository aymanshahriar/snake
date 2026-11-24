def draw(board_x, board_y, character):
    # Translate game_board coordinates to terminal coordinates based on 2 things:
    # 1) Terminal uses 1 based indexing, while the board uses 0 based indexing
    # 2) Each emoji is 2 columns wide
    terminal_x = (2 * board_x) + 1
    terminal_y = board_y + 1
    print(f'\033[{terminal_y};{terminal_x}H{character}\033[11;1H', flush=True, end='')


try:
    # enter alternate screen and disable mouse scrolling
    # also, make sure the cursor is at row 1 column 1 in the terminal
    print('\033[?1049h\033[?1000h\033[1:1H', end='', flush=True)

    board = [['⬜'] * 10 for _ in range(10)]

    for row in board:
        print(''.join(row))

    while True:
        usr_input = input()
        x_str, y_str = usr_input.split(',')
        x = int(x_str)
        y = int(y_str)
        draw(x, y, '🟩')
        #print(f'\033[3;6H🟩', flush=True, end='')
    
finally:
    # always make sure to exit alternate screen
    print('\033[?1049l\033[?]', end='', flush=True)

