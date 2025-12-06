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
































