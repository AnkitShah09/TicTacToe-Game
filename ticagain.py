from __future__ import print_function
import random
import os

def position(val,no):
	print("player 0='0' and player 1='X'")
	x = raw_input("Player %s's Move:"%(str(val)))
	os.system('cls')
	if int(x)<1 or int(x)>9 :
		print("Please enter Valid Positions.. :(")
		print_board()
		position(val,no)
	elif board[int(x)-1]!=0 and board[int(x)-1]!='X':
		board[int(x)-1]=player[ran_no]
		print()
	else:
		print("Value is already placed at that position...Enter another valid Value....!!!!!")
		print_board()
		position(val,no)

	if no>=4:
		game_logic(val,no)
		

def game_logic(val,no):
	for x in xrange(0,3):
		y=x*3
		if(board[x]==board[x+3]==board[x+6]==player[ran_no]): #Vertical
			game_logic_output(val,no)

		if(board[y]==board[y+1]==board[y+2]==player[ran_no]): #Horizontal
			game_logic_output(val,no)	

	if board[0]==board[4]==board[8]==player[ran_no] or board[2]==board[4]==board[6]==player[ran_no]:  #Diagonal
		game_logic_output(val,no)
		

def game_logic_output(val,no):
	os.system('cls')
	print("Player %s Won"%(str(val)))
	print_board()
	exit()


def print_board():
	print("      "+str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
	print("      "+"----------")
	print("      "+str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
	print("      "+"----------")
	print("      "+str(board[6])+" | "+str(board[7])+" | "+str(board[8]))
	print("      "+"----------\n\n\n")


# Program Starts From Here...
print("\t\t\t\t\t      - - - - - - - - - - - - - - - -")
print("\t\t\t\t\t      | Welcome To Tic Tac Toe Game |")
print("\t\t\t\t\t      - - - - - - - - - - - - - - - -")
board=[1,2,3,4,5,6,7,8,9]
print_board()
player=[0,'X']
no=0
ran_no=random.randint(0,1)
while no<9:
	position(ran_no,no)
	ran_no=(ran_no+1)%2
	print_board()
	no+=1
print("Game Draw...  :(")