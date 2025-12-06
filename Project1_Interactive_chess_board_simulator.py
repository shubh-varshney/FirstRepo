# **************Some context before coding*************************

#  Here we are making just a chess board representation not the actual chess game and using dictionary because there are some following benefits.
#  1. keys can't be used two times and each square can store only one piece on it .
# /and empty sqaure means it doesn't hold anything 


#  **********   Some rules**************

# we will represent each piece with 2 characer string 
# first character represent its color "b" and "w" 
#  and after that    Pawn-P, knight-N , Bishop-B , Rook- R, Queen - Q, King -K

#  and we represent the position with standard notation
# eg.--> a1,a2,f4 etc.
#   keys will identify the squares and the values identify the pieces .

#  absence of a key represent a empty square 



#  Step 1 --->
# Set up the program


import sys, copy

STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}


#  Step 2--->
# Create a chessboard template 

BOARD_TEMPLATE = """
   a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = '||'
BLACK_SQUARE = '  '

# The pairs of curly brackets represent places in the string where we’ll insert chess piece strings such as 'wR' or 'bQ'. If the square is empty, the program will insert the WHITE_SQUARE or BLACK_SQUARE string instead



# Step 3 --->Print the current chess board .

def print_chessboard(boards):
    squares = []
    is_white_square = True
    for y in '87654321':
        for x in 'abcdefgh':  # DEBUG: Show coordinates
            # print(x, y, is_white_square)  # DEBUG: Show coordinates
            if x+y in boards.keys():
             squares.append(boards[x+y])
            else:
              if is_white_square:
               squares.append(WHITE_SQUARE)
              else:
               squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square
    print(BOARD_TEMPLATE.format(*squares))   



print("It is an interactive chessboard")
print("By Shubh Varshney After reading automate the boring stuff")
print("Pieces:")
print(" w - white , b- Black")
print("P-Pawn , N -knight,B -Bishop,R - Rook,Q-Queen,K-King")
print('Commands:')
print('  move e2 e4 - Moves the piece at e2 to e4')
print('  remove e2 - Removes the piece at e2')
print('  set e2 wP - Sets square e2 to a white pawn')
print('  reset - Resets pieces back to their starting squares')
print('  clear - Clears the entire board')
print('  fill wP - Fills entire board with white pawns.')
print('  quit - Quits the program')



main_board = copy.copy(STARTING_PIECES)
while True:
  print_chessboard(main_board)
  print("Now please type your command below")
  response = input('>').split()
  if response[0]  == 'move':
    main_board[response[2]] = main_board[response[1]]
    del main_board[response[1]]
  elif response[0] == 'remove':
    del main_board[response[1]]
  elif response[0] == 'set':
        main_board[response[1]] = response[2]
  elif response[0] == 'reset':
        main_board = copy.copy(STARTING_PIECES)
  elif response[0] == 'clear':
        main_board = {}
  elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                main_board[x + y] = response[1]
  elif response[0] == 'quit':
        sys.exit()


#  finally it is of my own so happppppppy































# ********************Copy pasted stuff**************************
# import sys

# board = {}
# def empty_board(bo):
#     #this func initiates and empties a board
#     bo.clear()
#     angka = 8
#     for row in range(1, 9):
#         for column in range(1,9):

#             board.setdefault ((chr(ord("@")+column) + str(angka)), "___")
            
#         angka -= 1

# def print_board(bo):    
#     for cell, piece in bo.items():
#         if cell.startswith("H"):
#             print(piece)
#         else:
#             print(piece, end=" ")

# def default_board(bo):
#     for cell, piece in bo.items():
#         if cell == "A8":
#             bo[cell] = "B_r"
#         if cell == "B8":
#             bo[cell] = "B_n"
#         if cell == "C8":
#             bo[cell] = "B_b"
#         if cell == "D8":
#             bo[cell] = "B_q"
#         if cell == "E8":
#             bo[cell] = "B_k"
#         if cell == "F8":
#             bo[cell] = "B_b"
#         if cell == "G8":
#             bo[cell] = "B_n"
#         if cell == "H8":
#             bo[cell] = "B_r"
#         if cell == "A7":
#             bo[cell] = "B_p"
#         if cell == "B7":
#             bo[cell] = "B_p"
#         if cell == "C7":
#             bo[cell] = "B_p"
#         if cell == "D7":
#             bo[cell] = "B_p"
#         if cell == "E7":
#             bo[cell] = "B_p"
#         if cell == "F7":
#             bo[cell] = "B_p"
#         if cell == "G7":
#             bo[cell] = "B_p"
#         if cell == "H7":
#             bo[cell] = "B_p"
#         if cell == "H1":
#             bo[cell] = "W_r"
#         if cell == "G1":
#             bo[cell] = "W_n"
#         if cell == "F1":
#             bo[cell] = "W_b"
#         if cell == "E1":
#             bo[cell] = "W_k"
#         if cell == "D1":
#             bo[cell] = "W_q"
#         if cell == "C1":
#             bo[cell] = "W_b"
#         if cell == "B1":
#             bo[cell] = "W_n"
#         if cell == "A1":
#             bo[cell] = "W_r"
#         if cell == "A2":
#             bo[cell] = "W_p"
#         if cell == "B2":
#             bo[cell] = "W_p"
#         if cell == "C2":
#             bo[cell] = "W_p"
#         if cell == "D2":
#             bo[cell] = "W_p"
#         if cell == "E2":
#             bo[cell] = "W_p"
#         if cell == "F2":
#             bo[cell] = "W_p"
#         if cell == "G2":
#             bo[cell] = "W_p"
#         if cell == "H2":
#             bo[cell] = "W_p"        

# def move_piece(bo):
#     while True:    
#         move_what = input("Which piece you wanna move ")
#         if move_what == "!":
#             sys.exit()
#         elif move_what in board.values():
#             break
#         else:
#             print("that piece does not exist")
#     while True: 
#         move_from = input("From ")
#         if move_from == "!":
#             sys.exit()
#         elif bo.get(move_from) == move_what:
#             break
#         else:
#             print("That piece is not from there")
#     while True: 
#         move_to = input("to ")
#         if move_to == "!":
#             sys.exit()
#         elif move_to in bo:
#             break
#         else:
#             print("that's not a real location!")
#     bo[move_from] = "___"
#     bo[move_to] = move_what

# empty_board(board)

# default_board(board)

# print_board(board)


# color = "Black"
# while True:
#     if color == "White":
#         color = "Black"
#     else:
#         color = "White"
#     print("%s's turn to move" %color)
#     move_piece(board)
#     print_board(board)


# **************************************************************
