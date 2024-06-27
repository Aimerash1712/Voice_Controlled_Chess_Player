import pygame

pygame.init()
WIDTH = 800
HEIGHT = 700
BOARD_HEIGHT = 600
SQUARE_SIZE = 75

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 15)
medium_font = pygame.font.Font('freesansbold.ttf', 30)
big_font = pygame.font.Font('freesansbold.ttf', 40)
timer = pygame.time.Clock()
fps = 60

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []

# 0 - white's turn no selection: 1 - white's turn piece selected
# 2 - black's turn no selection: 3 - black's turn piece selected
turn_step = 0
selection = 100
valid_moves = []

# load in game piece images (queen, king, rook, bishop, knight, pawn)
black_queen = pygame.image.load('img/black queen.png')
black_queen = pygame.transform.scale(black_queen, (60, 60))
black_king = pygame.image.load('img/black king.png')
black_king = pygame.transform.scale(black_king, (60, 60))
black_rook = pygame.image.load('img/black rook.png')
black_rook = pygame.transform.scale(black_rook, (60, 60))
black_bishop = pygame.image.load('img/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (60, 60))
black_knight = pygame.image.load('img/black knight.png')
black_knight = pygame.transform.scale(black_knight, (60, 60))
black_pawn = pygame.image.load('img/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (60, 60))

white_queen = pygame.image.load('img/white queen.png')
white_queen = pygame.transform.scale(white_queen, (60, 60))
white_king = pygame.image.load('img/white king.png')
white_king = pygame.transform.scale(white_king, (60, 60))
white_rook = pygame.image.load('img/white rook.png')
white_rook = pygame.transform.scale(white_rook, (60, 60))
white_bishop = pygame.image.load('img/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (60, 60))
white_knight = pygame.image.load('img/white knight.png')
white_knight = pygame.transform.scale(white_knight, (60, 60))
white_pawn = pygame.image.load('img/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (60, 60))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


# draw main game board
def draw_board():
    for i in range(64):
        row = i // 8
        col = i % 8
        color = 'white' if (row + col) % 2 == 0 else 'brown'
        pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    pygame.draw.rect(screen, 'light blue', pygame.Rect(0, BOARD_HEIGHT, WIDTH, HEIGHT - BOARD_HEIGHT))
    pygame.draw.rect(screen, 'black', pygame.Rect(0, BOARD_HEIGHT, WIDTH, HEIGHT - BOARD_HEIGHT), 5)
    pygame.draw.rect(screen, 'black', pygame.Rect(600, 0, 200, HEIGHT), 5)

    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (10, BOARD_HEIGHT + 20))

    for i in range(9):
        pygame.draw.line(screen, 'black', (0, SQUARE_SIZE * i), (600, SQUARE_SIZE * i), 2)
        pygame.draw.line(screen, 'black', (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, BOARD_HEIGHT), 2)

    screen.blit(medium_font.render('FORFEIT', True, 'black'), (610, BOARD_HEIGHT + 30))


# draw pieces onto board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        screen.blit(white_images[index], (white_locations[i][0] * SQUARE_SIZE + 7, white_locations[i][1] * SQUARE_SIZE + 7))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * SQUARE_SIZE + 1, white_locations[i][1] * SQUARE_SIZE + 1,
                                                 SQUARE_SIZE, SQUARE_SIZE], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        screen.blit(black_images[index], (black_locations[i][0] * SQUARE_SIZE + 7, black_locations[i][1] * SQUARE_SIZE + 7))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * SQUARE_SIZE + 1, black_locations[i][1] * SQUARE_SIZE + 1,
                                                  SQUARE_SIZE, SQUARE_SIZE], 2)


# check valid moves for each piece
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations
    enemies_list = black_locations if color == 'white' else white_locations

    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position,

 color)
    for move in second_list:
        moves_list.append(move)
    return moves_list


# check bishop moves
def check_bishop(position, color):
    moves_list = []
    friends_list = white_locations if color == 'white' else black_locations
    enemies_list = black_locations if color == 'white' else white_locations

    directions = [(1, -1), (-1, -1), (1, 1), (-1, 1)]  # up-right, up-left, down-right, down-left
    for x, y in directions:
        path = True
        chain = 1
        while path:
            target = (position[0] + (chain * x), position[1] + (chain * y))
            if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                moves_list.append(target)
                if target in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check rook moves
def check_rook(position, color):
    moves_list = []
    friends_list = white_locations if color == 'white' else black_locations
    enemies_list = black_locations if color == 'white' else white_locations

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # down, up, right, left
    for x, y in directions:
        path = True
        chain = 1
        while path:
            target = (position[0] + (chain * x), position[1] + (chain * y))
            if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                moves_list.append(target)
                if target in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


# check valid knight moves
def check_knight(position, color):
    moves_list = []
    friends_list = white_locations if color == 'white' else black_locations
    enemies_list = black_locations if color == 'white' else white_locations

    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for dx, dy in targets:
        target = (position[0] + dx, position[1] + dy)
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check for valid moves for just selected piece
def check_valid_moves():
    options_list = white_options if turn_step < 2 else black_options
    valid_options = options_list[selection]
    return valid_options


# draw valid moves on screen
def draw_valid(moves):
    color = 'red' if turn_step < 2 else 'blue'
    for move in moves:
        pygame.draw.circle(screen, color, (move[0] * SQUARE_SIZE + 37, move[1] * SQUARE_SIZE + 37), 5)


# draw captured pieces on side of screen
def draw_captured():
    for i, captured_piece in enumerate(captured_pieces_white):
        index = piece_list.index(captured_piece)
        screen.blit(black_images[index], (625, 5 + 50 * i))
    for i, captured_piece in enumerate(captured_pieces_black):
        index = piece_list.index(captured_piece)
        screen.blit(white_images[index], (725, 5 + 50 * i))


# draw a flashing square around king if in check
def draw_check():
    if turn_step < 2 and 'king' in white_pieces:
        king_index = white_pieces.index('king')
        king_location = white_locations[king_index]
        if any(king_location in option for option in black_options):
            if counter < 15:
                pygame.draw.rect(screen, 'dark red', [king_location[0] * SQUARE_SIZE + 1, king_location[1] * SQUARE_SIZE + 1, SQUARE_SIZE, SQUARE_SIZE], 5)
    elif 'king' in black_pieces:
        king_index = black_pieces.index('king')
        king_location = black_locations[king_index]
        if any(king_location in option for option in white_options):
            if counter < 15:
                pygame.draw.rect(screen, 'dark blue', [king_location[0] * SQUARE_SIZE + 1, king_location[1] * SQUARE_SIZE + 1, SQUARE_SIZE, SQUARE_SIZE], 5)


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 300, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


# main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(fps)
    counter = (counter + 1) % 30
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // SQUARE_SIZE
            y_coord = event.pos[1] // SQUARE_SIZE
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3


                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()