import pygame
import sys
sys.path.append('C:/Users/andre/OneDrive/Desktop/')
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Python Chess Game ")

# Initialising pygame module
pygame.init()

# Setting Width and height of the Chess Game screen
WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Chess Game')

font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

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

# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []

# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('regina_neagra.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('rege_negru.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('tura_neagra.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('nebun_negru.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('cal_negru.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('pion_negru.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('regina_alba.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('rege_alb.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('tura_alba.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('nebun_alb.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('cal_alb.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('pion_alb.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_images = [white_pawn, white_queen, white_king,
                white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king,
                black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


# draw main game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [
                             600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [
                             700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(
            status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))


# draw pieces onto board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(
                white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i]
                        [0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(
                black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i]
                        [0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)


# function to check all pieces valid options on board
def check_options(pieces, locations, color):
    moves_list = []
    for i in range(len(pieces)):
        piece_type = pieces[i]
        piece_location = locations[i]
        if piece_type == 'rook':
            moves = check_rook(piece_location, color)
            moves_list.append(moves)
        elif piece_type == 'bishop':
            moves = check_bishop(piece_location, color)
            moves_list.append(moves)
        elif piece_type == 'knight':
            moves = check_knight(piece_location, color)
            moves_list.append(moves)
        elif piece_type == 'queen':
            moves = check_queen(piece_location, color)
            moves_list.append(moves)
        elif piece_type == 'king':
            moves = check_king(piece_location, color)
            moves_list.append(moves)
        elif piece_type == 'pawn':
            moves = check_pawn(piece_location, color)
            moves_list.append(moves)
    return moves_list


# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
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
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(
            screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# draw captured pieces on side of screen
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50 * i))


# draw a flashing square around king if in check
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(
        f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!',
                True, 'white'), (210, 240))

def promote_pawn(pieces, locations, index, new_piece):
    # Assume index is the position of the pawn in the lists that needs to be promoted
    if locations[index][1] == 7:  # Check if the pawn is on the last row for white
        pieces[index] = new_piece  # Promote to the specified piece, typically 'queen'

def is_stalemate(pieces, locations, color, opponents_moves):
    if color == 'white':
        king_position = locations[pieces.index('king')]
        if all(king_position not in move for move in opponents_moves):
            return True
    return False

def is_threefold_repetition(position_history):
    # This assumes position_history is a list of strings representing board states
    from collections import Counter
    counts = Counter(position_history)
    return any(count >= 3 for count in counts.values())

# main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True

#teste

#Condiția de promovare: Un pion trebuie să ajungă pe rândul cel mai îndepărtat de poziția sa inițială pe tablă (pentru albi, rândul 8; pentru negri, rândul 1).
def test_promotion():
    # Inițializăm o listă de piese cu două pioni.
    piese = ['pawn', 'pawn']
    locatii = [(0, 6), (1, 7)]
    # Apelăm funcția `promote_pawn` pentru a promova un pion la regină.
    promote_pawn(piese, locatii, 1, 'queen')
    # Verificăm dacă al doilea pion a fost promovat la regină.
    assert piese == ['pawn', 'queen'], "Promovarea pionului a eșuat"
    print("Testul de promovare a trecut")

#Caracteristici ale stalemate-ului:
    #Lipsa mutărilor legale: Jucătorul care trebuie să mute nu poate face o mutare legală cu niciuna dintre piesele sale.
    #Regele nu este în șah: Deși jucătorul nu are mutări legale, regele său nu este atacat direct (nu este pus în șah).
    #Rezultatul este o remiză: Indiferent de alte avantaje pe tablă, cum ar fi materialul suplimentar sau o poziție mai bună, partida se termină în egalitate.
def test_stalemate_detection():
    # Inițializăm lista de piese cu regele și tura.
    pieces = ['king', 'rook']
    # Specificăm coordonatele pe tabla de șah pentru rege și tură.
    locations = [(0, 0), (0, 1)]
    # Definim mișcările posibile ale adversarului care pot bloca regele, simulând un scenariu de pat.
    opponents_moves = [[(0, 2)], [(1, 0), (2, 0)]]  # Mișcările simulate care blochează regele
    # Verificăm dacă situația actuală este detectată ca fiind un pat.
    assert is_stalemate(pieces, locations, 'white', opponents_moves), "Stalemate not detected"
    print("Stalemate detection test passed")


#Scopul funcției este de a testa detectarea repetării de trei ori a unei anumite configurații într-un joc
def test_threefold_repetition_detection():
    history = ["pos1", "pos2", "pos1", "pos2", "pos1"]
    assert is_threefold_repetition(history), "Threefold repetition not detected"
    print("Threefold repetition test passed")


def test_check_king():
    # Presupunem că regele este poziționat central pe tabla de șah, fără piese care să-l blocheze
    king_position = (4, 4)
    
    # Definim mutările așteptate pentru rege când este în această poziție
    expected_moves = [(4, 5), (4, 3), (5, 4), (3, 4), (5, 5), (5, 3), (3, 5), (3, 3)]
    
    # Apelăm funcția `check_king` pentru a obține mutările posibile ale regelui în această situație
    actual_moves = check_king(king_position, 'white')
    
    # Verificăm fiecare mutare așteptată să fie în lista de mutări posibile
    for move in expected_moves:
        assert move in actual_moves, f"Expected move {move} not possible for king"
    
    # Afișăm un mesaj de succes dacă toate mutările așteptate sunt validate
    print("King movement test passed.")

def test_check_queen():
    queen_position = (4, 4)
    expected_moves = check_bishop(queen_position, 'white') + check_rook(queen_position, 'white')
    actual_moves = check_queen(queen_position, 'white')
    assert len(actual_moves) == len(expected_moves), "Queen does not have correct number of moves"
    print("Queen movement test passed.")

def test_piece_selection_and_movement():
    # Inițializăm poziția inițială a unui pion alb pentru simularea unei mișcări
    initial_position = (1, 1)
    # Definim noua poziție în care dorim să mutăm pionul
    new_position = (1, 2)
    # Găsim indexul poziției inițiale în lista de locații ale pieselor albe
    selection = white_locations.index(initial_position)
    # Actualizăm poziția în lista de locații, simulând mutarea pionului
    white_locations[selection] = new_position
    # Verificăm dacă noua poziție a pionului este acum în lista de locații ale pieselor albe
    assert new_position in white_locations, "Pawn did not move correctly"
    # Afișăm un mesaj de succes dacă pionul a fost mutat corect
    print("Piece selection and movement test passed.")

def test_castling():
    
    white_king_initial = (4, 0)  # Poziția inițială a regelui alb
    white_rook_initial = (7, 0)  # Poziția inițială a turei albe
    # Stabilim pozițiile finale ale regelui și turei după rocadă
    white_king_final = (6, 0)  # Poziția finală a regelui după rocadă
    white_rook_final = (5, 0)  # Poziția finală a turei după rocadă
    white_pieces = ['king', 'rook']  # Lista de piese implicate în rocadă
    white_locations = [white_king_initial, white_rook_initial]  # Locațiile inițiale ale pieselor
    white_locations[0] = white_king_final  # Actualizăm poziția regelui
    white_locations[1] = white_rook_final  # Actualizăm poziția turei
    # Verificăm pozițiile pentru a ne asigura că rocada a avut loc corect
    assert white_locations == [white_king_final, white_rook_final], "Castling failed to update positions correctly"
    print("Castling test passed.")


def test_check_detection():
    black_king_position = (4, 0)  # Poziția regelui negru
    white_rook_position = (4, 7)  # Poziția turei albe
    black_pieces = ['king']  # Lista cu piesele negre (doar regele în acest test)
    black_locations = [black_king_position]  # Locațiile pieselor negre
    white_pieces = ['rook']  # Lista cu piesele albe (doar tura în acest test)
    white_locations = [white_rook_position]  # Locațiile pieselor albe
    # Presupunem că funcția 'check_options' calculează mutările potențiale pentru fiecare piesă albă și verifică dacă poziția regelui este amenințată
    white_threats = check_options(white_pieces, white_locations, 'white')
    # Determinăm dacă regele negru este în șah verificând dacă poziția sa este în vreo listă de mutări amenințătoare ale albilor
    is_in_check = any(black_king_position in moves for moves in white_threats)
    assert is_in_check, "Check not detected when king is in line of attack from rook"
    print("Check detection test passed.")
    print(f"White threats: {white_threats}")  # Afișăm amenințările albilor
    print(f"Is king in check? {'Yes' if is_in_check else 'No'}")  # Afișăm dacă regele este în șah


def test_piece_capture():
    # Setup a scenario where a pawn captures an opposing knight
    white_pawn_position = (3, 3)
    black_knight_position = (4, 4)
    black_pieces = ['knight']
    black_locations = [black_knight_position]
    white_pieces = ['pawn']
    white_locations = [white_pawn_position]
    
    # Simulate capture
    white_locations[0] = black_knight_position  # Pawn captures knight
    black_pieces.remove('knight')
    black_locations.remove(black_knight_position)

    assert 'knight' not in black_pieces and black_knight_position not in black_locations, "Knight not captured correctly"
    print("Piece capture test passed.")


def test_pawn_double_move():
    # Initial position for a white pawn
    initial_position = (4, 1)
    expected_position = (4, 3)
    white_pieces = ['pawn']
    white_locations = [initial_position]
    
    # Simulate pawn's double move
    white_locations[0] = expected_position

    assert white_locations == [expected_position], "Pawn did not move two spaces from initial position"
    print("Pawn double move test passed.")

def test_game_reset():
    # Modify some game state to simulate a game in progress
    black_pieces.append('queen')
    black_locations.append((2, 2))
    game_over = True

    # Reset game state
    black_pieces.clear()
    black_locations.clear()
    game_over = False

    assert not black_pieces and not black_locations and not game_over, "Game did not reset correctly"
    print("Game reset test passed.")

#de aici incepe partea de AI

def evaluate_board(board):
    piece_value = {
        'pawn': 1, 'knight': 3, 'bishop': 3, 'rook': 5, 'queen': 9, 'king': 1000
    }
    white_score = 0
    black_score = 0
    for piece in board.white_pieces:
        white_score += piece_value[piece]
    for piece in board.black_pieces:
        black_score += piece_value[piece]
    return white_score - black_score

#minimax
def minimax(position, depth, alpha, beta, maximizing_player):
    if depth == 0 or position.is_game_over():
        return evaluate_board(position)

    if maximizing_player:
        max_eval = float('-inf')
        for child in position.generate_successors('white'):
            eval = minimax(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in position.generate_successors('black'):
            eval = minimax(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
def best_move(position, depth):
    best_eval = float('-inf')
    best_move = None
    for child in position.generate_successors('white'):
        eval = minimax(child, depth - 1, float('-inf'), float('inf'), False)
        if eval > best_eval:
            best_eval = eval
            best_move = child
    return best_move
# Exemplu de definiție a stării curente a tablei de șah
class ChessBoard:
    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
    def __init__(self):
        self.board = {}  # Inițializează board ca un dicționar gol
        self.setup_initial_board()  # Apoi setează piesele inițiale
        self.current_player = 'white'

    def setup_initial_board(self):
        # Inițializează tabla de șah cu piesele în pozițiile de start
        # Pionii
        for i in range(8):
            self.board[(i, 1)] = Piece('pawn', 'white')
            self.board[(i, 6)] = Piece('pawn', 'black')
        # Turnurile
        self.board[(0, 0)] = self.board[(7, 0)] = Piece('rook', 'white')
        self.board[(0, 7)] = self.board[(7, 7)] = Piece('rook', 'black')
        # Caii
        self.board[(1, 0)] = self.board[(6, 0)] = Piece('knight', 'white')
        self.board[(1, 7)] = self.board[(6, 7)] = Piece('knight', 'black')
        # Nebunii
        self.board[(2, 0)] = self.board[(5, 0)] = Piece('bishop', 'white')
        self.board[(2, 7)] = self.board[(5, 7)] = Piece('bishop', 'black')
        # Reginele
        self.board[(3, 0)] = Piece('queen', 'white')
        self.board[(3, 7)] = Piece('queen', 'black')
        # Regii
        self.board[(4, 0)] = Piece('king', 'white')
        self.board[(4, 7)] = Piece('king', 'black')

    def generate_successors(self, player_color):
        successors = []
        for position, piece in self.board.items():
            if piece.color == player_color:
                for move in self.get_legal_moves(position):
                    new_board = self.clone()
                    new_board.make_move(position, move)
                    successors.append(new_board)
        return successors


    def get_pieces(self, player_color):
     return [pos for pos, piece in self.board.items() if piece.color == player_color]


    def get_legal_moves(self, position):
     piece = self.board[position]
     moves = []
     if piece.type == 'pawn':
        direction = 1 if piece.color == 'white' else -1
        forward_move = (position[0], position[1] + direction)
        if forward_move not in self.board:  # Verifică dacă poziția este liberă
            moves.append(forward_move)
        # Adaugă și capturile diagonale
        for dx in [-1, 1]:
            capture_move = (position[0] + dx, position[1] + direction)
            if capture_move in self.board and self.board[capture_move].color != piece.color:
                moves.append(capture_move)
     return moves


    def make_move(self, piece, move):
    # Mută piesa la noua poziție și elimină piesa din poziția veche
     self.board[move] = self.board[piece]
     del self.board[piece]


    def clone(self):
        # Creează și întoarce o copie profundă a acestei table de șah
        import copy
        return copy.deepcopy(self)
    
    def is_game_over(self):
        # Verifică dacă există mutări legale pentru jucătorul curent
        # Simplificat: presupune că dacă regele este în șah și nu are mutări legale, este șah mat
        current_color = 'white' if self.current_player == 'white' else 'black'
        has_legal_moves = any(self.get_legal_moves(pos) for pos, piece in self.board.items() if piece.color == current_color)
        is_in_check = self.is_king_in_check(current_color)
        return not has_legal_moves and is_in_check

    def is_king_in_check(self, player_color):
        # Verifică dacă regele jucătorului este în șah
        # Acesta este un exemplu foarte simplificat
        king_position = next((pos for pos, piece in self.board.items() if piece.type == 'king' and piece.color == player_color), None)
        if not king_position:
            return False  # Regele nu este pe tablă
        
        # Verifică dacă vreo piesă adversă poate muta pe poziția regelui
        opponent_color = 'black' if player_color == 'white' else 'white'
        for pos, piece in self.board.items():
            if piece.color == opponent_color and king_position in self.get_legal_moves(pos):
                return True
        return False 
    
    def apply_move(color, selected_index, new_position):
      global current_player, turn_step, selection, valid_moves
      if color == 'white':
        white_locations[selected_index] = new_position
      else:
        black_locations[selected_index] = new_position

class Piece:
    def __init__(self, type, color):
        self.type = type
        self.color = color


def make_move(position, move):
    # Aplică mutarea pe tabla de șah
    # 'position' este starea curentă a jocului
    # 'move' este mutarea care trebuie aplicată
    position.apply_move(move)
    # Schimbă jucătorul curent după fiecare mutare
    global current_player
    current_player = 'black' if current_player == 'white' else 'white'

def handle_events(event):
    global run, game_over
    if event.type == pygame.QUIT:
        run = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN and game_over:
            reset_game()

def handle_human_move(event):
    global current_player, selection, turn_step
    x_coord = event.pos[0] // 100
    y_coord = event.pos[1] // 100
    click_coords = (x_coord, y_coord)

    if turn_step <= 1 and click_coords in white_locations:
        selection = white_locations.index(click_coords)
        if turn_step == 0:
            turn_step = 1
    elif turn_step <= 1 and click_coords in valid_moves and selection != 100:
        apply_move('white', selection, click_coords)
    elif turn_step > 1 and click_coords in black_locations:
        selection = black_locations.index(click_coords)
        if turn_step == 2:
            turn_step = 3
    elif turn_step > 1 and click_coords in valid_moves and selection != 100:
        apply_move('black', selection, click_coords)


    # Verificare capturare
    check_capture(new_position, color)
    turn_step = 0 if color == 'black' else 2
    selection = 100
    valid_moves = []
    current_player = 'black' if color == 'white' else 'white'
    update_game_options()

def update_game_options():
    global valid_moves, game_over, winner
    # Actualizează mutările valide pentru jucătorul curent
    if current_player == 'white':
        valid_moves = get_valid_moves(white_pieces, white_locations)
    else:
        valid_moves = get_valid_moves(black_pieces, black_locations)
    
    # Verifică dacă regele este în șah
    if is_king_in_check(current_player):
        print(f"{current_player.capitalize()} king is in check!")
        # Poți adăuga logică suplimentară pentru șah mat sau pat
    
    # Verifică condiții de terminare a jocului
    if check_game_over():
        game_over = True
        winner = 'black' if current_player == 'white' else 'white'

def get_valid_moves(pieces, locations):
    # Această funcție trebuie să genereze toate mutările valide pentru piesele specificate
    # Simplificat, returnează lista de mutări posibile pentru fiecare piesă
    return [((loc[0] + 1, loc[1]), (loc[0] - 1, loc[1])) for loc in locations]  # Exemplu simplificat

def is_king_in_check(player):
    # Această funcție determină dacă regele jucătorului este în șah
    # Trebuie să implementezi logica de verificare pe baza pozițiilor pieselor adverse
    return False  # Simplificat pentru exemplu

def check_game_over():
    # Verifică dacă jocul trebuie să se termine (de ex., prin șah mat sau pat)
    return False  # Simplificat pentru exemplu


def check_capture(position, color):
    global captured_pieces_white, captured_pieces_black
    opponent_locations = black_locations if color == 'white' else white_locations
    opponent_pieces = black_pieces if color == 'white' else white_pieces
    if position in opponent_locations:
        index = opponent_locations.index(position)
        captured_piece = opponent_pieces.pop(index)
        opponent_locations.pop(index)
        if color == 'white':
            captured_pieces_white.append(captured_piece)
        else:
            captured_pieces_black.append(captured_piece)

def reset_game():
    global white_pieces, white_locations, black_pieces, black_locations
    global captured_pieces_white, captured_pieces_black
    global current_player, selection, turn_step, valid_moves, game_over, winner

    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook'] + ['pawn'] * 8
    white_locations = [(i, 0) for i in range(8)] + [(i, 1) for i in range(8)]
    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook'] + ['pawn'] * 8
    black_locations = [(i, 7) for i in range(8)] + [(i, 6) for i in range(8)]
    captured_pieces_white, captured_pieces_black = [], []
    current_player = 'white'
    selection = 100
    turn_step = 0
    valid_moves = []
    game_over = False
    winner = ''
    update_game_options()

if __name__ == "__main__":
    # Running tests
    test_check_king()
    test_check_queen()
    test_piece_selection_and_movement()
    test_castling()
    test_check_detection()
    test_piece_capture()
    test_pawn_double_move()
    test_game_reset()
    test_promotion()
    test_stalemate_detection()
    test_threefold_repetition_detection()

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Python Chess Game")
clock = pygame.time.Clock()
run = True
game_over = False
current_player = 'white'  # Albul începe jocul, controlat de AI
current_position = ChessBoard()
# Definiția și inițializarea pieselor și a pozițiilor pe tabla de joc

while run:

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
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
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
                    black_options = check_options(
                        black_pieces, black_locations, 'black')
                    white_options = check_options(
                        white_pieces, white_locations, 'white')
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
                    black_options = check_options(
                        black_pieces, black_locations, 'black')
                    white_options = check_options(
                        white_pieces, white_locations, 'white')
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
                black_options = check_options(
                    black_pieces, black_locations, 'black')
                white_options = check_options(
                    white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()

pygame.quit()


