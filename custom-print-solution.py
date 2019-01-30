#set up a for loop to go through each of 
#the elements in the outer list (each of which is a row of our board) and print them.

board = []
for i in range(5):
  board.append(['O'] * 5)
def print_board(board_in):
  for row in board:
    print row 
    
print_board(board)
