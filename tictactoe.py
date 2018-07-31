from __future__ import print_function
import random
import os

def position(val,no):
	print("player 0='0' and player 1='X'")
	x = raw_input("Player %s's Move:"%(str(val))).split(',')

	if (int(x[0])-1)>=3 or (int(x[1])-1)>=3:
		os.system('cls')
		print("Please enter Valid Positions.. :(")
		print_board()
		position(val,no)
	elif board[int(x[0])-1][int(x[1])-1]==" ":
		os.system('cls')
		board[int(x[0])-1][int(x[1])-1]=player[ran_no]
		print()
	else:
		os.system('cls')
		print("Value is already placed at that position...Enter another valid Value....!!!!!")
		print_board()
		position(val,no)

	if no>=4:
		game_logic(val,no)
		

def game_logic(val,no):
	if board[0][0]==board[0][1]==board[0][2]==player[ran_no]:    #Horizontal  
		game_logic_output(val,no)

	elif board[1][0]==board[1][1]==board[1][2]==player[ran_no]:  #Horizontal
		game_logic_output(val,no)

	elif board[2][0]==board[2][1]==board[2][2]==player[ran_no]:  #Horizontal
		game_logic_output(val,no)

	elif board[0][0]==board[1][0]==board[2][0]==player[ran_no]:   #Vertical
		game_logic_output(val,no)

	elif board[0][1]==board[1][1]==board[2][1]==player[ran_no]:   #Vertical
		game_logic_output(val,no)

	elif board[0][2]==board[1][2]==board[2][2]==player[ran_no]:   #Vertical
		game_logic_output(val,no)

	elif board[0][0]==board[1][1]==board[2][2]==player[ran_no]:  #Diagonal
		game_logic_output(val,no)

	elif board[0][2]==board[1][1]==board[2][0]==player[ran_no]:  #Diagonal
		game_logic_output(val,no)
		

def game_logic_output(val,no):
	os.system('cls')
	print("Player %s Won"%(str(val)))
	print_board()
	exit()


def print_board():
	print("\n      "+"1 "+"  2 "+"  3 "+"\n")
	print("1     "+str(board[0][0])+" | "+str(board[0][1])+" | "+str(board[0][2]))
	print("      "+"----------")
	print("2     "+str(board[1][0])+" | "+str(board[1][1])+" | "+str(board[1][2]))
	print("      "+"----------")
	print("3     "+str(board[2][0])+" | "+str(board[2][1])+" | "+str(board[2][2]))
	print("      "+"----------\n\n\n")


# Program Starts From Here...
print("\t\t\t\t\t      - - - - - - - - - - - - - - - -")
print("\t\t\t\t\t      | Welcome To Tic Tac Toe Game |")
print("\t\t\t\t\t      - - - - - - - - - - - - - - - -")
print("\nEnter positions like 1,1 ; 2,0 ; 3,0\n")
board=[[" "]*3,[" "]*3,[" "]*3]
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