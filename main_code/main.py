# Importing Libraries
import pygame
import time

# Calling the construtor
pygame.init()

# Setting game screen dimensions
screen = pygame.display.set_mode((500, 500))

# Setting header title caption and icon
pygame.display.set_caption("TicTokToe")
header_icon = pygame.image.load("grid_icon.png")
pygame.display.set_icon(header_icon)

# fonts settings
font = pygame.font.Font('Pixeboy.ttf', 50)

# Load background image
tictac_grid_white = pygame.image.load("grid_thin_sprite_white.png")
tictac_grid_black = pygame.image.load("grid_thin_sprite_black.png")
title_background = pygame.image.load("background_red.png")

#Title Card
title_card = pygame.image.load("Title_Card.png")
# Load player1/player2 images
cross_marker = pygame.image.load("cross.png")
circle_marker = pygame.image.load("circle.png")
# Load dark_mode_button images
dark_mode_on = pygame.image.load("switch_on.png")
dark_mode_off = pygame.image.load("switch_off.png")
# Load menu_buttons images
pvc_button_red = pygame.image.load("PVC_red.png")
pvp_button_red = pygame.image.load("PVP_red.png")
exit_button_red = pygame.image.load("EXIT_red.png")
###orange variant
pvc_button_orange = pygame.image.load("PVC_orange.png")
pvp_button_orange = pygame.image.load("PVP_orange.png")
exit_button_orange = pygame.image.load("EXIT_orange.png")
# Load home_button images
home_button_black = pygame.image.load("home_black.png")
home_button_white = pygame.image.load("home_white.png")
# Load winning line images
win_line_horizontal = pygame.image.load("line_horizontal.png")
win_line_vertical = pygame.image.load("line_vertical.png")
win_line_diagonal_foward = pygame.image.load("line_diagonal_foward.png")
win_line_diagonal_backward = pygame.image.load("line_diagonal_backward.png")

# sprite offset
sprite_to_grid_offset = 18


# clicked cell corresponding sreen pixel range
cell_pos = (((100, 200), (100, 200)),
            ((200, 300), (100, 200)),
            ((300, 400), (100, 200)),
            ((100, 200), (200, 300)),
            ((200, 300), (200, 300)),
            ((300, 400), (200, 300)),
            ((100, 200), (300, 400)),
            ((200, 300), (300, 400)),
            ((300, 400), (300, 400)))

#checks cell each entry
cell_entry_check = [False]*9

#Player X input function
def playerX_move(user_input):
    clicked_pos = user_input
    for j in range(9):
        if cell[j] == 'X':
            cell_entry_check[j] = True
        elif cell[j] == 'O':
            cell_entry_check[j] = True
    for i in range(9):
        if clicked_pos[0] > cell_pos[i][0][0] and clicked_pos[0] < cell_pos[i][0][1] and clicked_pos[1] > cell_pos[i][1][0] and clicked_pos[1] < cell_pos[i][1][1] and cell_entry_check[i] == False:
            cell[i] = 'X'
            cell_entry_check[i] = True
    
            break

  

#Player O input function
def playerO_move(user_input):
    clicked_pos = user_input
    #clicked_cell = None
    for j in range(9):
        if cell[j] == 'X':
            cell_entry_check[j] = True
        elif cell[j] == 'O':
            cell_entry_check[j] = True
    for i in range(9):
        if clicked_pos[0] > cell_pos[i][0][0] and clicked_pos[0] < cell_pos[i][0][1] and clicked_pos[1] > cell_pos[i][1][0] and clicked_pos[1] < cell_pos[i][1][1] and cell_entry_check[i] == False:
            cell[i] = 'O'
            cell_entry_check[i] = True
            break

 

#Displays player O and player x sprites function
def player_sprite_display(cell):
    for i in range(9):
        if cell[i] == 'X':
            screen.blit(cross_marker, [
                        cell_pos[i][0][0]+sprite_to_grid_offset, cell_pos[i][1][0]+sprite_to_grid_offset])
        elif cell[i] == 'O':
            screen.blit(circle_marker, [
                        cell_pos[i][0][0]+sprite_to_grid_offset, cell_pos[i][1][0]+sprite_to_grid_offset])
        else:
            pass

#Function for dark mode
def darkmode(user_input):
    global current_colour
    global dark_button_input_check
    clicked_pos = user_input
    dark_button_input_check = clicked_pos[0] > 432 and clicked_pos[
        0] < 496 and clicked_pos[1] > 0 and clicked_pos[1] < 64
    if dark_button_input_check:
        if current_colour == white:
            current_colour = black
        elif current_colour == black:
            current_colour = white

#Function to check cell inputs
def test(a, b, c, who):
    global move
    if cell[a] == who and cell[b] == who and cell[c] == str(c):
        cell[c] = 'O'
        move = True
    elif cell[a] == who and cell[b] == str(b) and cell[c] == who:
        cell[b] = 'O'
        move = True
    elif cell[a] == str(a) and cell[b] == who and cell[c] == who:
        cell[a] = 'O'
        move = True

#Function for A.I
def computer_move():
    global move
    # time.sleep(0.5)
    move = False

    # completion moves
    test(0, 1, 2, 'O')  # 1st row completion check
    if not move:
        test(3, 4, 5, 'O')  # mid row completion check
    if not move:
        test(6, 7, 8, 'O')  # 3rd row completion check
    if not move:
        test(0, 3, 6, 'O')  # 1st column completion check
    if not move:
        test(1, 4, 7, 'O')  # mid column completion check
    if not move:
        test(2, 5, 8, 'O')  # 3rd column completion check
    if not move:
        test(0, 4, 8, 'O')  # left diagonal completion check
    if not move:
        test(2, 4, 6, 'O')  # right diagonal completion check
    # done shifting index to zero covention

    # prevention moves
    if not move:
        test(0, 1, 2, 'X')  # 1st row completion check
    if not move:
        test(3, 4, 5, 'X')  # mid row completion check
    if not move:
        test(6, 7, 8, 'X')  # 3rd row completion check
    if not move:
        test(0, 3, 6, 'X')  # 1st column completion check
    if not move:
        test(1, 4, 7, 'X')  # mid column completion check
    if not move:
        test(2, 5, 8, 'X')  # 3rd column completion check
    if not move:
        test(0, 4, 8, 'X')  # left diagonal completion check
    if not move:
        test(2, 4, 6, 'X')  # right diagonal completion check
    # done shifting index to zero covention

    # non completion moves
    if not move:
        if cell[0] == '0':
            cell[0] = 'O'
        elif cell[2] == '2':
            cell[2] = 'O'
        elif cell[6] == '6':
            cell[6] = 'O'
        elif cell[8] == '8':
            cell[8] = 'O'
        elif cell[4] == '4':
            cell[4] = 'O'
        elif cell[1] == '1':
            cell[1] = 'O'
        elif cell[3] == '3':
            cell[3] = 'O'
        elif cell[5] == '5':
            cell[5] = 'O'
        elif cell[7] == '7':
            cell[7] = 'O'
    # done shifting index to zero covention

#Function to check any win
def check_win():
    global win
    win = False
    if (cell[0] == cell[1] == cell[2]):
        screen.blit(win_line_horizontal, [100, 100])
        win = True
    elif (cell[3] == cell[4] == cell[5]):
        screen.blit(win_line_horizontal, [100, 200])
        win = True
    elif (cell[6] == cell[7] == cell[8]):
        screen.blit(win_line_horizontal, [100, 300])
        win = True
    elif (cell[0] == cell[3] == cell[6]):
        screen.blit(win_line_vertical, [100, 100])
        win = True
    elif (cell[1] == cell[4] == cell[7]): 
        screen.blit(win_line_vertical, [200, 100])
        win = True        
    elif (cell[2] == cell[5] == cell[8]):
        screen.blit(win_line_vertical, [300, 100])
        win = True
    elif (cell[0] == cell[4] == cell[8]):
        screen.blit(win_line_diagonal_backward, [100, 100])
        win = True
    elif (cell[2] == cell[4] == cell[6]):
        screen.blit(win_line_diagonal_foward, [100, 100])
        win = True
    return win

#Function to check any draw
def check_draw():
    global draw
    draw = False
    if cell[0] != '0' and cell[1] != '1' and cell[2] != '2' and cell[3] != '3' and cell[4] != '4' and cell[5] != '5' and cell[6] != '6' and cell[7] != '7' and cell[8] != '8':
        draw = True
    return draw

#Function to flip turns
def flip_turn():
    global turn_of
    if turn_of == 'X':
        turn_of = 'O'
    else:
        turn_of = 'X'
    return turn_of

#Function for win/lose/draw logic
def game_logic():
    global turn_of2
    check_win()
    if win:
        print('Game won by', turn_of2)
        return "win"
    check_draw()
    if draw:
        print('Game Draw !')
        # time.sleep(0.1)
        return "draw"

    # flip_turn()



# numbering each cell
cell = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
res = ''

#White and Black colour variable
white = (255, 255, 255)
black = (0, 0, 0)

#Current colour initialized to white
current_colour = black

#Variable to store who's turn is it
turn_of = 'X'
turn_of2 = 'X'

#Text variables
win_text = font.render("", False, (0, 0, 0))
gamemode_text = font.render("", False, (0, 0, 0))

# Main pogram loops
menu_running= True
game_running = True

#Game Loop
while game_running:

    #Menu loop
    while menu_running:
        cell = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        cell_entry_check=[False]*9
        win_text = font.render("",False, (0, 0, 255), current_colour)
        # looping through every event happened in 1 main loop cycle
        for event in pygame.event.get():
            
            #screen.fill(current_colour)
            screen.blit(title_background, [0, 0])
            screen.blit(title_card, [120, 0])
            # check if close button( X ) has been pressed on header of game window
            if event.type == pygame.QUIT:
                game_running = False
                menu_running = False
            gamemode = ''
            screen.blit(pvc_button_red, [200, 250])
            screen.blit(pvp_button_red, [200, 300])
            screen.blit(exit_button_red, [200, 350])
            # get mouse cursor position
            mouse_pos = pygame.mouse.get_pos()

            if mouse_pos[0] > 200 and mouse_pos[0] < (200+100) and mouse_pos[1] > 250 and mouse_pos[1] < (250+50):
                screen.blit(pvc_button_orange, [200, 250])
            elif mouse_pos[0] > 100 and mouse_pos[0] < (200+100) and mouse_pos[1] > 200 and mouse_pos[1] < (300+50):
                screen.blit(pvp_button_orange, [200, 300])        
            elif mouse_pos[0] > 100 and mouse_pos[0] < (200+100) and mouse_pos[1] > 350 and mouse_pos[1] < (350+50):
                screen.blit(exit_button_orange, [200, 350])   

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] > 200 and mouse_pos[0] < (200+100) and mouse_pos[1] > 250 and mouse_pos[1] < (250+50):
                    gamemode = 'pve'
                    menu_running = False
                elif mouse_pos[0] > 100 and mouse_pos[0] < (200+100) and mouse_pos[1] > 200 and mouse_pos[1] < (300+50):
                    gamemode = 'pvp'
                    menu_running = False    
                elif mouse_pos[0] > 100 and mouse_pos[0] < (200+100) and mouse_pos[1] > 350 and mouse_pos[1] < (350+50):
                    gamemode = 'exit'
                    menu_running = False
            pygame.display.update()

    if gamemode == 'pve':

        for event in pygame.event.get():

            # check if close button( X ) has been pressed on header of game window
            if event.type == pygame.QUIT:
                game_running = False

            screen.fill(current_colour)
            if current_colour == white:
                screen.blit(dark_mode_off, [500-68, 0])
                screen.blit(tictac_grid_white, [100, 100])
                screen.blit(home_button_black, [5, 5])
            elif current_colour == black:
                screen.blit(dark_mode_on, [500-68, 0])
                screen.blit(tictac_grid_black, [100, 100])
                screen.blit(home_button_white, [5, 5])
                
            gamemode_text = font.render("PLAYER(X) Vs. AI(O)",
                            False, (0, 0, 255), current_colour)
            # get mouse cursor position
            mouse_pos = pygame.mouse.get_pos()
            #dark_mode_check
            if event.type == pygame.MOUSEBUTTONDOWN:
                darkmode(mouse_pos)
            #home_botton check    
            if mouse_pos[0] > 5 and mouse_pos[0] < (64+5) and mouse_pos[1] > 5 and mouse_pos[1] < (64+5):    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_running=True
                    break
            #turn check
            if turn_of == 'X':
                if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] > 100 and mouse_pos[0] < 400 and mouse_pos[1] > 100 and mouse_pos[1] < 400:
                    playerX_move(mouse_pos)
                    turn_of = 'O'
                    turn_of2 = 'X'
            elif turn_of == 'O':
                    computer_move()
                    turn_of = 'X'
                    turn_of2 = 'O'

            # X|0 sprite placement
            player_sprite_display(cell)
            # Win/Draw check
            res = game_logic()
            if res == 'win':
                win_text = font.render("Game Won by : "+turn_of2,
                                   False, (0, 0, 255), current_colour)
            elif res == 'draw':
                win_text = font.render("Game Draw!!!", False,
                                   (0, 255, 0), current_colour)
            
            # draw text on screen
            screen.blit(win_text, [120, 10])
            screen.blit(gamemode_text, [75, 500-50])
            # Updates the screen upon the occurrence of an event
            pygame.display.update()
            if res == "win" or res == "draw":
                time.sleep(2)
                menu_running=True
                break

    elif gamemode=='pvp':
        for event in pygame.event.get():

            # check if close button( X ) has been pressed on header of game window
            if event.type == pygame.QUIT:
                game_running = False

            screen.fill(current_colour)
            if current_colour == white:
                screen.blit(dark_mode_off, [500-68, 0])
                screen.blit(tictac_grid_white, [100, 100])
                screen.blit(home_button_black, [5, 5])
            elif current_colour == black:
                screen.blit(dark_mode_on, [500-68, 0])
                screen.blit(tictac_grid_black, [100, 100])
                screen.blit(home_button_white, [5, 5])
            gamemode_text = font.render("PLAYER1 (X) Vs. PLAYER2 (O)",
                            False, (0, 0, 255), current_colour)
            # get mouse cursor position
            mouse_pos = pygame.mouse.get_pos()
            #dark_mode_check
            if event.type == pygame.MOUSEBUTTONDOWN:
                darkmode(mouse_pos)
            #home_botton check    
            if mouse_pos[0] > 5 and mouse_pos[0] < (64+5) and mouse_pos[1] > 5 and mouse_pos[1] < (64+5):    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_running=True
                    break
            #turn check
            if turn_of == 'X':
                if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] > 100 and mouse_pos[0] < 400 and mouse_pos[1] > 100 and mouse_pos[1] < 400:
                    playerX_move(mouse_pos)
                    turn_of = 'O'
                    turn_of2 = 'X'
            elif turn_of == 'O':
                if event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] > 100 and mouse_pos[0] < 400 and mouse_pos[1] > 100 and mouse_pos[1] < 400:
                    playerO_move(mouse_pos)
                    turn_of = 'X'
                    turn_of2 = 'O'

            # X|0 sprite placement
            player_sprite_display(cell)
            # Win/Draw check
            res = game_logic()
            if res == 'win':
                win_text = font.render("Game Won by : "+turn_of2,
                                   False, (0, 0, 255), current_colour)
            elif res == 'draw':
                win_text = font.render("Game Draw!!!", False,
                                   (0, 255, 0), current_colour)
            
            # draw text on screen
            screen.blit(win_text, [120, 10])
            screen.blit(gamemode_text, [0, 500-50])
            # Updates the screen upon the occurrence of an event
            pygame.display.update()
            if res == "win" or res == "draw":
                time.sleep(2)
                menu_running=True
                break


    elif gamemode == 'exit':
        game_running = False
