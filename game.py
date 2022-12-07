"""
Check if the game is a draw
Check wins
"""
import random

def PrintBoard(board):
	"""
	Displays the board to the console

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board
	"""
	print(str(board[1]) + " | " + str(board[2]) + " | " + str(board[3]))
	print("---------")
	print(str(board[4]) + " | " + str(board[5]) + " | " + str(board[6]))
	print("---------")
	print(str(board[7]) + " | " + str(board[8]) + " | " + str(board[9]))

def IsEmpty(board, position):
	"""
	Checks if a slot in the board is empty

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board
	position : int
		The position we want to check is empty 

	Returns
	-------
	bool
		True if the position in the board is empty
	"""
	if board[position] != 'X' and board[position] != 'O':
		return True
	else:
		return False

def IsOnBoard(position):
	"""
	Checks if a position is on the board

	Parameters
	----------
	position : int
		The position we want to check if it is on the board

	Returns
	-------
	bool
		True if the position is on the board
	"""
	if position >= 1 and position < 10:
		return True
	else:
		return False

def InsertPiece(board, position, piece):
	"""
	Inserts a piece into the board, modifying the board in-place

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board
	position : int
		The position we want to insert the piece into
	piece : str
		The piece to insert into the board

	Returns
	-------
	bool
		True if the piece could be placed in a valid position
	"""
	if IsOnBoard(position):
		# If the position is on the board
		if IsEmpty(board, position):
			# If the position is empty
			board[position] = piece
			return True
		else:
			print(f"Position {position} is taken, please try again")
			return False
	else:
		print(f"Position {position} is not on the board!")
		print("Positions are represented by integers from 1 to 9 inclusive.\n")
		return False

def PlayerMove(board, piece, player_name):
	"""
	Prompts the human player to take their turn

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board
	piece : str
		The piece to insert into the board
	player_name : str
		The name of the player
	"""
	while True:
		try:
			PrintBoard(board)
			position = int(input(f"{player_name}, enter a new position for {piece}: "))
			if not InsertPiece(board, position, piece):
				PlayerMove(board, piece, player_name)
			break
		except:
			print("Please enter an integer...")

def ComputerMove(board, piece):
	"""
	Prompts the computer to take their turn

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board
	piece : str
		The piece to insert into the board
	"""
	position = AI(board, piece)
	if not InsertPiece(board, position, piece):
		ComputerMove(board, piece)

def CheckWins(board):
	"""
	Checks if the game has been won

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board

	Returns
	-------
	winner : str/None
		The piece of the winner of the game or None if there has been no winner
	"""
	h = CheckHorizontal(board)
	v = CheckVerical(board)
	d = CheckDiagonal(board)
	if h is not None:
		return h
	elif v is not None:
		return v
	else:
		return d

def CheckHorizontal(board):
	"""
	Checks if the game has been won by 3 in a row horizontally

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board

	Returns
	-------
	winner : str/None
		The piece of the winner of the game or None if there has been no winner
	"""
	for j in range(0,3,1):
		if board[3*j + 1] == board[3*j + 2] and board[3*j + 2] == board[3*j + 3]:
			if board[3*j + 1] == 'X':
				return 'X'
			else:
				return 'O'
	return None

def CheckVerical(board):
	"""
	Checks if the game has been won by 3 in a row verically

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board

	Returns
	-------
	winner : str/None
		The piece of the winner of the game or None if there has been no winner
	"""
	for j in range(0,3,1):
		if board[j + 1] == board[j + 4] and board[j + 4] == board[j + 7]:
			if board[j + 1] == 'X':
				return 'X'
			else:
				return 'O'
	return None

def CheckDiagonal(board):
	"""
	Checks if the game has been won by 3 in a row diagonally

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board

	Returns
	-------
	winner : str/None
		The piece of the winner of the game or None if there has been no winner
	"""
	if (board[1] == board[5] and board[5] == board[9]) or (board[3] == board[5] and board[5] == board[7]):
		if board[5] == 'X':
			return 'X'
		else:
			return 'O'
	return None

def CheckFull(board):
	"""
	Checks if all the spots on the board have been filled

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board

	Returns
	-------
	bool
		True if the board is full
	"""
	for i in range(1,10,1):
		if board[i] == i:
			return False
	return True

def CheckGameOver(board, players):
	"""
	Checks if the game is over

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board
	"""
	winner = CheckWins(board)
	if winner is not None:
		winner_name = players[winner]
		print(f"{winner_name} won!")
		return True
	elif CheckFull(board):
		print("The game was a draw!")
		return True
	else:
		return False

def ToggleMarker(marker):
	if marker == 'X':
		return 'O'
	else:
		return 'X'

def MiniMax(board, marker):
	"""
	Returns the Minimax value of the board

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board
	market : str
		The marker of the current player

	Returns
	minimax_value : int
		The minimax value value of the board
	"""
	# Base case
	winner = CheckWins(board)
	if winner == 'X':
		minimax_value = 1
		return minimax_value
	elif winner == 'O':
		minimax_value = -1
		return minimax_value
	elif CheckFull(board):
		minimax_value = 0
		return minimax_value

	if marker == 'X':
		minimax_value = -999
		for i in range(1,10):
			if IsEmpty(board, i):
				board[i] = marker
				score = MiniMax(board, ToggleMarker(marker))
				board[i] = i
				if score > minimax_value:
					minimax_value = score
		return minimax_value
	else:
		minimax_value = 999
		for i in range(1,10):
			if IsEmpty(board, i):
				board[i] = marker
				score = MiniMax(board, ToggleMarker(marker))
				board[i] = i
				if score < minimax_value:
					minimax_value = score
		return minimax_value

def AI(board, computer_marker):
	"""
	Returns the position the computer should move to

	Parameters
	----------
	board : dict of {int : str}
		A dictionary representing the board
	computer_marker : str
		The marker the AI/computer is playing with

	Returns
	-------
	best_move : int
		The best position that the AI can move to
	"""
	# Initialise the best_score variable and best_move variables
	best_score = None
	best_move = None
	if computer_marker == 'X':
		# If the computer is playing as X, initialise it to a very low number
		best_score = -999
	else:
		# If the computer is playing as O, initialise it ot a very high number
		best_score = 999

	for i in range(1,10):
		if IsEmpty(board, i):
			board[i] = computer_marker
			score = MiniMax(board, ToggleMarker(computer_marker))
			board[i] = i
			if computer_marker == 'X':
				if score > best_score:
					best_move = i
					best_score = score
			else:
				if score < best_score:
					best_move = i
					best_score = score
	return best_move

board = {i:i for i in range(1,10,1)}
player_marker = 'X'
computer_marker = 'O'
player_name = "Alex"

players = {player_marker:player_name, computer_marker:"Computer"}

move_count = 0
while not CheckGameOver(board, players):
	if move_count % 2 == 0:
		PlayerMove(board,'X',"Alex")
	else:
		ComputerMove(board,'O')
	move_count += 1