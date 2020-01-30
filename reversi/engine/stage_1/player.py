import random	
import time
import sys
import math
import copy
import pickle
import feature_dict
import os

def sorted_moves(data):
	list1 = [ item[0] for item in data ]
	list2 = [ item[1] for item in data ] 
	list1, list2 = (list(x) for x in zip(*sorted(zip(list1, list2), key=lambda pair: pair[1], reverse = True)))
	return [ [list1[i], list2[i]] for i in range(len(data)) ]	
def print_board(board):
	i=0
	board_to_be_printed = [ '-' for x in range(64)]
	for x in board:
		if x==0:
			board_to_be_printed[i] = '-'
		elif x==1:
			board_to_be_printed[i] = 'X'
		elif x==-1:
			board_to_be_printed[i] = 'O'
		i +=1
	i=0	
	for y in range(8):
		print(board_to_be_printed[8*(8-y)-8 :8*(8-y)])
	print('#########################')
	return
	
def sorted_moves(data):
	list1 = [ item[0] for item in data ]
	list2 = [ item[1] for item in data ] 
	list1, list2 = (list(x) for x in zip(*sorted(zip(list1, list2), key=lambda pair: pair[1], reverse = True)))
	return [ [list1[i], list2[i]] for i in range(len(data)) ]
	
		
def neighbors_N_function(pos,board):
	row = divmod(pos,8)[0]
	neighbors = []
	if row == 8:
		return neighbors
	else: 
		for i in range(7-row):
			neighbors.append(board[pos+8*(i+1)])
	return	neighbors

def neighbors_S_function(pos,board):
	row = divmod(pos,8)[0]
	neighbors = []
	if row == 0:
		return neighbors
	else:
		for i in range(row):
			neighbors.append(board[pos-8-8*i])
	return neighbors
	
def neighbors_W_function(pos,board):
	column = divmod(pos,8)[1]
	neighbors = []
	if column == 0:
		return neighbors
	else:
		for i in range(column):
			neighbors.append(board[pos-1-i])
	return neighbors

def neighbors_E_function(pos,board):
	column = divmod(pos,8)[1]
	neighbors = []
	if column == 7:
		return neighbors
	else:
		for i in range(7-column):
			neighbors.append(board[pos+1+i])
	return neighbors
	
def neighbors_SE_function(pos,board):
	row, column = divmod(pos,8)
	neighbors = []
	if column == 7:
		return neighbors
	if row == 0:
		return neighbors
	for i in range(min(row,7-column)):
		neighbors.append(board[pos-7-7*i])
	return neighbors
		
def neighbors_SW_function(pos,board):
	row,column = divmod(pos,8)
	neighbors = []
	if column == 0:
		return neighbors
	if row == 0:
		return neighbors
	for i in range(min(row,column)):
		neighbors.append(board[pos-9-9*i])
	return neighbors
	
def neighbors_NW_function(pos,board):
	row, column = divmod(pos,8)
	neighbors = []
	if column == 0:
		return neighbors
	if row == 7:
		return neighbors
	for i in range(min(7-row,column)):
		neighbors.append(board[pos + 7+ 7*i])
	return neighbors
	
def neighbors_NE_function(pos,board):
	row, column = divmod(pos,8)
	neighbors = []
	if column == 7:
		return neighbors
	if 	row == 7:
		return neighbors
	for i in range(min(7-row,7-column)):
		neighbors.append(board[pos + 9 + 9*i])
	return neighbors
	
def is_legal_move(i, board, color): # and look at that, this one does. Beats me :)

	if board[i] != 0:
		return False

	if neighbors_N[i]:
		if board[neighbors_N[i][0]] == -color:
			for x in neighbors_N[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					return True

	if neighbors_E[i]:
		if board[neighbors_E[i][0]] == -color:
			for x in neighbors_E[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					return True

	if neighbors_S[i]:
		if board[neighbors_S[i][0]] == -color:
			for x in neighbors_S[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					return True

	if neighbors_W[i]:
		if board[neighbors_W[i][0]] == -color:
			for x in neighbors_W[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					return True

	if neighbors_SE[i]:
		if board[neighbors_SE[i][0]] == -color:
			for x in neighbors_SE[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					return True

	if neighbors_SW[i]:
		if board[neighbors_SW[i][0]] == -color:
			for x in neighbors_SW[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					return True

	if neighbors_NE[i]:
		if board[neighbors_NE[i][0]] == -color:
			for x in neighbors_NE[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					return True

	if neighbors_NW[i]:
		if board[neighbors_NW[i][0]] == -color:
			for x in neighbors_NW[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					return True
	
	return False
						
					
def make_move(i, board, color):
	
	new_board = board[:]
	new_board[i]= color
	
	if neighbors_N[i]:
		if board[neighbors_N[i][0]] == -color:
			for x in neighbors_N[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					for y in range(neighbors_N[i].index(x)):
						new_board[neighbors_N[i][y]] = color
					break

	if neighbors_E[i]:
		if board[neighbors_E[i][0]] == -color:
			for x in neighbors_E[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					for y in range(neighbors_E[i].index(x)):
						new_board[neighbors_E[i][y]] = color
					break
					
	if neighbors_S[i]:
		if board[neighbors_S[i][0]] == -color:
			for x in neighbors_S[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					for y in range(neighbors_S[i].index(x)):
						new_board[neighbors_S[i][y]] = color
					break
					
	if neighbors_W[i]:
		if board[neighbors_W[i][0]] == -color:
			for x in neighbors_W[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					for y in range(neighbors_W[i].index(x)):
						new_board[neighbors_W[i][y]] = color
					break
					
	if neighbors_SE[i]:
		if board[neighbors_SE[i][0]] == -color:
			for x in neighbors_SE[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					for y in range(neighbors_SE[i].index(x)):
						new_board[neighbors_SE[i][y]] = color
					break
					
	if neighbors_SW[i]:
		if board[neighbors_SW[i][0]] == -color:
			for x in neighbors_SW[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					for y in range(neighbors_SW[i].index(x)):
						new_board[neighbors_SW[i][y]] = color
					break
					
	if neighbors_NE[i]:
		if board[neighbors_NE[i][0]] == -color:
			for x in neighbors_NE[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					for y in range(neighbors_NE[i].index(x)):
						new_board[neighbors_NE[i][y]] = color
					break
					
	if neighbors_NW[i]:
		if board[neighbors_NW[i][0]] == -color:
			for x in neighbors_NW[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					for y in range(neighbors_NW[i].index(x)):
						new_board[neighbors_NW[i][y]] = color
					break
					
	return new_board

def attempt_to_make_move(i, board, color): #delete that silly board copying
	
	
	legal = False
	flipped_pieces = []
	
	if neighbors_N[i]:
		if board[neighbors_N[i][0]] == -color:
			for x in neighbors_N[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					legal = True
					for y in range(neighbors_N[i].index(x)):
						flipped_pieces.append(neighbors_N[i][y])
					break

	if neighbors_E[i]:
		if board[neighbors_E[i][0]] == -color:
			for x in neighbors_E[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					legal = True
					for y in range(neighbors_E[i].index(x)):
						flipped_pieces.append(neighbors_E[i][y])
					break
					
	if neighbors_S[i]:
		if board[neighbors_S[i][0]] == -color:
			for x in neighbors_S[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					legal = True
					for y in range(neighbors_S[i].index(x)):
						flipped_pieces.append(neighbors_S[i][y])
					break
					
	if neighbors_W[i]:
		if board[neighbors_W[i][0]] == -color:
			for x in neighbors_W[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					legal = True
					for y in range(neighbors_W[i].index(x)):
						flipped_pieces.append(neighbors_W[i][y])
					break
					
	if neighbors_SE[i]:
		if board[neighbors_SE[i][0]] == -color:
			for x in neighbors_SE[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					legal = True
					for y in range(neighbors_SE[i].index(x)):
						flipped_pieces.append(neighbors_SE[i][y])
					break
					
	if neighbors_SW[i]:
		if board[neighbors_SW[i][0]] == -color:
			for x in neighbors_SW[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					legal = True
					for y in range(neighbors_SW[i].index(x)):
						flipped_pieces.append(neighbors_SW[i][y])
					break
					
	if neighbors_NE[i]:
		if board[neighbors_NE[i][0]] == -color:
			for x in neighbors_NE[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					legal = True
					for y in range(neighbors_NE[i].index(x)):
						flipped_pieces.append(neighbors_NE[i][y])
					break
					
	if neighbors_NW[i]:
		if board[neighbors_NW[i][0]] == -color:
			for x in neighbors_NW[i]:
				if board[x] == 0:
					break
				if board[x] == color:
					legal = True
					for y in range(neighbors_NW[i].index(x)):
						flipped_pieces.append(neighbors_NW[i][y])
					break
					
	if legal:
		new_board = board[:]
		new_board[i] = color
		for flipped_piece in flipped_pieces:
			new_board[flipped_piece] = color
		return new_board			
	return False	
	
def attempt_to_make_move_modify(i, board,  color, neighbors, legal):
	
	overall_legal = False
	for j in range(8):
		if board[neighbors[j][i][0]] == -color:
			for k in range(1,7):
				if board[neighbors[j][i][k]] == color:
					overall_legal = True
					legal = True
					break	
				if board[neighbors[j][i][k]] == 0:
					legal = False
					break
				legal = False
			if legal:
				for z in range(k):
					board[neighbors[j][i][z]] = color
					
	if overall_legal:
		board[i] = color
		return True			
	return False
	
	
def attempt_to_make_move_and_features_modify(i, board, feature_values, feature_indices, color, neighbors,legal):
	
	overall_legal = False
	for j in range(8):
		if board[neighbors[j][i][0]] == -color:
			for k in range(1,7):
				if board[neighbors[j][i][k]] == color:
					overall_legal = True
					legal = True
					break	
				if board[neighbors[j][i][k]] == 0:
					legal = False
					break
				legal = False
			if legal:
				
				for z in range(k):
					to_be_flipped = neighbors[j][i][z]
					board[to_be_flipped] = color
					# print('we are flipping', to_be_flipped, 'disk')
					for feature_to_be_updated,by_how_much in feature_indices[to_be_flipped]:
						# print( feature_to_be_updated,by_how_much )
						# input()
						feature_values[feature_to_be_updated] += color*2*by_how_much
							
	if overall_legal:
		board[i] = color
		# print('we are flipping', i, 'disk')
		for feature_to_be_updated,by_how_much in feature_indices[i]:
			# print( feature_to_be_updated,by_how_much )
			# input()
			feature_values[feature_to_be_updated] += color*by_how_much
		
		return True			
	return False	
	
	
def possible_moves(board, color):
	valid_moves = []
	for i in range(64):
		if board[i] != 0:
			continue
		if is_legal_move(i, board, color):
			valid_moves.append(i)
	return valid_moves

def move_exists(board, color):
	for i in range(64):
		if board[i] != 0:
			continue
		if is_legal(i, board, color):
			return True
	return False	

class Node(object):

	def __init__(self, node_board, node_parent, color):
		
		self.games = 0.1
		self.score = 0.
		self.color = color
		self.win_chance = None
		self.board = None
		self.parent = node_parent
		self.board = node_board
		self.children = None
	
	def simulate(self):
		self.games += 1
		value_to_backpropagate = play_duel_game(self.board,self.color)
		self.score += value_to_backpropagate
		self.backpropagate(value_to_backpropagate)
	
	def backpropagate(self, value_to_backpropagate):
		if self.parent != None:
			self.parent.games += 1
			self.parent.score += value_to_backpropagate
			self.parent.backpropagate(value_to_backpropagate)
			
	def choose(self):
		if self.children != None:
			try:
				action_values = [branch.action_value() for branch in self.children]
			except:
				print_board(self.board)
				print(self.children)
			self.children[action_values.index(max(action_values))].choose()
		else:
			if self.games < 3:
				self.simulate()
			else:
				self.expand()
	
	def expand(self):
		global depth
		current_depth = current_node.board.count(0)-self.board.count(0)
		if current_depth > depth:
			print('current depth is', current_depth)
			depth = current_depth
		moves = possible_moves(self.board, self.color)
		if moves:
			self.children = [Node(attempt_to_make_move(move, self.board, self.color), self, -self.color) for move in moves]
		else:
			if possible_moves(self.board, -self.color):
				self.children = [Node(self.board, self, -self.color)] 
			else:
				self.simulate()
				
			
	def action_value(self):
		if self.parent.color == 1:
			return self.score/self.games + math.sqrt(2* math.log(self.parent.games)/ self.games) 
		if self.parent.color == -1:
			return (self.games-self.score)/self.games + math.sqrt(2* math.log(self.parent.games)/ self.games) 


def play_duel_game(board_start,color):			

	board = board_start[:]
	end_game_counter = 0
	
	print('game starts with board')
	print_board(board)
	
	depth_search_first_player = 5
	depth_search_second_player = 5
	end_depth_search_first_player = 10
	end_depth_search_second_player = 10
	
	for move in range(80):
		
		moves_hero = possible_moves(board, color)
		if len(moves_hero) > 0:
			end_game_counter = 0
			if board.count(0) <= end_depth_search_first_player:
				result_hero = alphabeta_score(board, end_depth_search_first_player, -100000, 100000, color, 1, 0, board.count(0))
			if board.count(0) > end_depth_search_first_player:
				result_hero = alphabeta_table(board, calculate_board_features(board[:]), depth_search_first_player, -100000, 100000, color, 1, 0, board.count(0))
			
			empties = board.count(0)
			
			if empties == 5:
				global_training_board_list[0].append([board[:], calculate_board_features(board[:])[:], result_hero[0] ])
			if empties == 10:
				global_training_board_list[1].append([board[:], calculate_board_features(board[:])[:], result_hero[0] ])
			if empties == 15:
				global_training_board_list[2].append([board[:], calculate_board_features(board[:])[:], result_hero[0] ])
			if empties == 20:
				global_training_board_list[3].append([board[:], calculate_board_features(board[:])[:], result_hero[0] ])
			if empties == 25:
				global_training_board_list[4].append([board[:], calculate_board_features(board[:])[:], result_hero[0] ])
			if empties == 30:
				global_training_board_list[5].append([board[:], calculate_board_features(board[:])[:], result_hero[0] ])
			if empties == 35:
				global_training_board_list[6].append([board[:], calculate_board_features(board[:])[:], result_hero[0] ])
			if empties == 40:
				global_training_board_list[7].append([board[:], calculate_board_features(board[:])[:], result_hero[0] ])
			if empties == 45:
				global_training_board_list[8].append([board[:], calculate_board_features(board[:])[:], result_hero[0] ])
			if empties == 50:
				global_training_board_list[9].append([board[:], calculate_board_features(board[:])[:], result_hero[0] ])
				
			attempt_to_make_move_modify(result_hero[1], board, color, neighbors,  False)
			
			
			
			print(result_hero)
			# print_board(board)
			# input()
			
			
		elif end_game_counter == 2:								
			break
		else:
			end_game_counter += 1
		
		moves_villain = possible_moves(board, -color)	
		if len(moves_villain) > 0:
			end_game_counter = 0
			if board.count(0) <= end_depth_search_second_player:
				result_villain = alphabeta_score(board, end_depth_search_second_player, -100000, 100000, -color, 1, 0, board.count(0))
			if board.count(0) > end_depth_search_second_player:	
				result_villain = alphabeta_table(board, calculate_board_features(board[:]), depth_search_second_player , -100000, 100000, -color, 1, 0,board.count(0))
			
			empties = board.count(0)
			
			if empties == 5:
				global_training_board_list[0].append([board[:], calculate_board_features(board[:])[:], result_villain[0] ])
			if empties == 10:
				global_training_board_list[1].append([board[:], calculate_board_features(board[:])[:], result_villain[0] ])
			if empties == 15:
				global_training_board_list[2].append([board[:], calculate_board_features(board[:])[:], result_villain[0] ])
			if empties == 20:
				global_training_board_list[3].append([board[:], calculate_board_features(board[:])[:], result_villain[0] ])
			if empties == 25:
				global_training_board_list[4].append([board[:], calculate_board_features(board[:])[:], result_villain[0] ])
			if empties == 30:
				global_training_board_list[5].append([board[:], calculate_board_features(board[:])[:], result_villain[0] ])
			if empties == 35:
				global_training_board_list[6].append([board[:], calculate_board_features(board[:])[:], result_villain[0] ])
			if empties == 40:
				global_training_board_list[7].append([board[:], calculate_board_features(board[:])[:], result_villain[0] ])
			if empties == 45:
				global_training_board_list[8].append([board[:], calculate_board_features(board[:])[:], result_villain[0] ])
			if empties == 50:
				global_training_board_list[9].append([board[:], calculate_board_features(board[:])[:], result_villain[0] ])
			
			attempt_to_make_move_modify(result_villain[1], board, -color, neighbors, False)#random.choice(moves_villain)
			
			
			
			print(result_villain)
			# print_board(board)
			# input()
			
			
		elif end_game_counter == 2:
			break
		else:
			end_game_counter += 1

	# print('result of the game is', sum(board))
	# if sum(board) > 0:
		# return 1.
	# elif sum(board)<0:
		# return 0.
	# elif sum(board)==0:
		# return 0.5
	game_result = sum(board)
	
	
	for stage in range(10):
		global_training_board_list[stage][-1][2] = (global_training_board_list[stage][-1][2]+game_result)/2
	
	
	return (sum(board)+64)/128
	
	# if sum(board) > 0:
		# return 1.
	# elif sum(board)<0:
		# return 0.
	# elif sum(board)==0:
		# return 0.5
	
	# return (sum(board) + 64)/128


def play_random_game(board_start,color):			

	board = side_board[:]
	end_game_counter = 0
	
	# print('game starts with board')
	# print_board(board)
	
	depth_search_first_player = 1
	depth_search_second_player = 1
	end_depth_search_first_player = 1
	end_depth_search_second_player = 1
	
	
	for move in range(80):
		
		moves_hero = possible_moves(board, color)
		if len(moves_hero) > 0:
			end_game_counter = 0
			if board.count(0) <= end_depth_search_first_player:
				result_hero = alphabeta_score(board, end_depth_search_first_player, -100000, 100000, color, color, 0, board.count(0))
			if board.count(0) > end_depth_search_first_player:
				result_hero = alphabeta_table(board, calculate_board_features(board[:]), depth_search_first_player, -100000, 100000, color, color, 0, board.count(0))
			
			
			attempt_to_make_move_modify(result_hero[1], board, color, neighbors,  False)
	
			
			print(result_hero)
			print_board(board)
			input()
			
			
		elif end_game_counter == 2:								
			break
		else:
			end_game_counter += 1
		
		moves_villain = possible_moves(board, -color)	
		if len(moves_villain) > 0:
			end_game_counter = 0
			if board.count(0) <= end_depth_search_second_player:
				result_villain = alphabeta_score(board, end_depth_search_second_player, -100000, 100000, -color, -color, 0, board.count(0))
			if board.count(0) > end_depth_search_second_player:	
				result_villain = alphabeta_table(board, calculate_board_features(board[:]), depth_search_second_player , -100000, 100000, -color, -color, 0,board.count(0))
			
		
			attempt_to_make_move_modify(random.choice(moves_villain), board, -color, neighbors, False)#random.choice(moves_villain)
			
		
			
			print(result_villain)
			print_board(board)
			input()
			
			
		elif end_game_counter == 2:
			break
		else:
			end_game_counter += 1

	# print('result of the game is', sum(board))
	# if sum(board) > 0:
		# return 1.
	# elif sum(board)<0:
		# return 0.
	# elif sum(board)==0:
		# return 0.5
	
	return (sum(board)+64)/128
	
	# if sum(board) > 0:
		# return 1.
	# elif sum(board)<0:
		# return 0.
	# elif sum(board)==0:
		# return 0.5
	
	# return (sum(board) + 64)/128
			
def play_human_game(board_start,color):			

	board = side_board[:]
	end_game_counter = 0
	
	# print('game starts with board')
	# print_board(board)
	
	depth_search_first_player = 10
	depth_search_second_player = 1
	end_depth_search_first_player = 12
	end_depth_search_second_player = 12
	
	
	for move in range(80):
		
		moves_hero = possible_moves(board, color)
		if len(moves_hero) > 0:
			end_game_counter = 0
			if board.count(0) <= end_depth_search_first_player:
				result_hero = alphabeta_score(board, end_depth_search_first_player, -100000, 100000, color, color, 0, board.count(0))
			if board.count(0) > end_depth_search_first_player:
				result_hero = alphabeta_table(board, calculate_board_features(board[:]), depth_search_first_player, -100000, 100000, color, color, 0, board.count(0))
			
			
			attempt_to_make_move_modify(result_hero[1], board, color, neighbors,  False)
	
			
			print('predicted result:', result_hero[0], 'move chosen:', move_encoding_number_to_string(result_hero[1]) )
			print_board(board)
			# input()
			print('enter human move (e.g. h4)')
			
		elif end_game_counter == 2:								
			break
		else:
			end_game_counter += 1
		
		moves_villain = possible_moves(board, -color)	
		if len(moves_villain) > 0:
			end_game_counter = 0
			if board.count(0) <= end_depth_search_second_player:
				result_villain = alphabeta_score(board, end_depth_search_second_player, -100000, 100000, -color, -color, 0, board.count(0))
			if board.count(0) > end_depth_search_second_player:	
				result_villain = alphabeta_table(board, calculate_board_features(board[:]), depth_search_second_player , -100000, 100000, -color, -color, 0,board.count(0))
			
			input_from_user = input()
			move_recorded = 0
				
			move_recorded = move_encoding_string_to_number(input_from_user)
			
			
			attempt_to_make_move_modify(move_recorded, board, -color, neighbors, False)#random.choice(moves_villain)
			
		
			
			# print(result_villain)
			# print_board(board)
			# input()
			
			
		elif end_game_counter == 2:
			break
		else:
			end_game_counter += 1

	# print('result of the game is', sum(board))
	# if sum(board) > 0:
		# return 1.
	# elif sum(board)<0:
		# return 0.
	# elif sum(board)==0:
		# return 0.5
	
	return (sum(board)+64)/128
	
	# if sum(board) > 0:
		# return 1.
	# elif sum(board)<0:
		# return 0.
	# elif sum(board)==0:
		# return 0.5
	
	# return (sum(board) + 64)/128
			
def board_evaluation_table(board, starting_feature_values, empties, game_ended):
	global global_node_count
	global_node_count+=1
	if empties == 0 or game_ended == 2:
		return sum(board)
		
	stage = max( (empties-3)//5, 0)
	if stage > 9:
		stage = 9
		
	total = 0
	for feature, dict in zip(starting_feature_values, dicts):
		total += dict[feature][stage]
	return total #+ random.choice([-1,0,1])			

def move_ordering(starting_board, empty_squares,how_many_plies_more): #we give it a list
	move_range = killer_move_table[empty_squares]
	if how_many_plies_more > 3:
		if tuple(starting_board) in hash_table[empty_squares]:
			for move in hash_table[empty_squares][tuple(starting_board)]:
				move_range.remove(move)
				move_range.append(move)
	return reversed(move_range)

def move_ordering_score(starting_board, empty_squares): #we give it a list
	return reversed(killer_move_table[empty_squares])
	
def alphabeta_table(starting_board, starting_feature_values,how_many_plies_more, alpha, beta, color, max_player, game_ended, empties):
	#this code is for checking whether feature changing is correct

	# print_board(starting_board)
	# reference_features = calculate_board_features(starting_board[:])
	# for feature1, feature2 in zip(starting_feature_values,reference_features):
			# print(feature1,'\t\t', feature2, '\t\t', feature1 ==feature2 )
	# input()



	if how_many_plies_more == 0 or game_ended == 2: 
		return [ max_player*board_evaluation_table(starting_board, starting_feature_values,empties,game_ended), [] ]#board_evaluation_table  
	if color == max_player:
		v = -100000
		best_move = []
		move_found = False
		board = starting_board[:] 
		feature_values = starting_feature_values[:]
	
		# move_range = range(64)
		move_range = move_ordering(starting_board, empties, how_many_plies_more)
		for next_move_candidate in move_range:
			if board[next_move_candidate] != 0:
				continue
			legal = attempt_to_make_move_and_features_modify(next_move_candidate, board, feature_values, feature_indices, color,neighbors,  False)
			if legal:
				move_found = True
				game_ended = 0
				
				
				g = alphabeta_table(board, feature_values ,how_many_plies_more-1, alpha, beta, -color ,max_player ,game_ended, empties-1)
				board = starting_board[:] 
				feature_values =  starting_feature_values[:]
				if g[0] > v:
					v = g[0]
					best_move = next_move_candidate
					if how_many_plies_more > 3:
						if tuple(starting_board) not in hash_table[empties]:
							hash_table[empties][tuple(starting_board)] = [best_move]
						else:
							if best_move in hash_table[empties][tuple(starting_board)]:
								hash_table[empties][tuple(starting_board)].remove(best_move)
								hash_table[empties][tuple(starting_board)].append(best_move)
							else:
								hash_table[empties][tuple(starting_board)].append(best_move)
				alpha = max(alpha, v)
				if beta <= alpha:        
					killer_move_table[empties].remove(best_move)    ##############
					killer_move_table[empties].append(best_move) ################
					break
		if move_found:
			return [v, best_move]
		else:
			game_ended += 1
			v = max(v, alphabeta_table(board,feature_values, how_many_plies_more, alpha, beta, -color, max_player,game_ended, empties)[0] )
			return [v, best_move ] 
	
	else:
		v = 100000
		best_move = []
		move_found = False
		board = starting_board[:] 
		feature_values =  starting_feature_values[:]
		# move_range = range(64) ####
		move_range = move_ordering(starting_board, empties,how_many_plies_more)##
		for next_move_candidate in move_range:
			if board[next_move_candidate] != 0:
				continue
			legal = attempt_to_make_move_and_features_modify(next_move_candidate, board, feature_values, feature_indices, color, neighbors, False)
			
			if legal:
				move_found = True
				game_ended = 0
			
				g = alphabeta_table(board, feature_values,how_many_plies_more-1, alpha, beta, -color, max_player,game_ended, empties-1)
				board = starting_board[:] 
				feature_values =  starting_feature_values[:]
				if g[0] < v:
					v = g[0]
					best_move = next_move_candidate
					if how_many_plies_more > 3:
						if tuple(starting_board) not in hash_table[empties]:
							hash_table[empties][tuple(starting_board)] = [best_move]
						else:
							if best_move in hash_table[empties][tuple(starting_board)]:
								hash_table[empties][tuple(starting_board)].remove(best_move)
								hash_table[empties][tuple(starting_board)].append(best_move)
							else:
								hash_table[empties][tuple(starting_board)].append(best_move)
				beta = min(beta, v)
				if beta <= alpha:               #############
					killer_move_table[empties].remove(best_move)     #############
					killer_move_table[empties].append(best_move)     #############
					break
		if move_found:
			return [v, best_move]
		else:
			game_ended += 1
			v = min(v, alphabeta_table(board,feature_values, how_many_plies_more, alpha, beta, -color, max_player,game_ended, empties)[0] )
			return [v,best_move]

def alphabeta_score(starting_board, how_many_plies_more, alpha, beta, color, max_player, game_ended, empties):
	#this code is for checking whether feature changing is correct

	# print_board(starting_board)
	# reference_features = calculate_board_features(starting_board[:])
	# for feature1, feature2 in zip(starting_feature_values,reference_features):
			# print(feature1,'\t\t', feature2, '\t\t', feature1 ==feature2 )
	# input()



	if how_many_plies_more == 0 or game_ended == 2: 
		global global_node_count
		global_node_count+=1
		return [ max_player*sum(starting_board), [] ]#board_evaluation_table  
		
	if color == max_player:
		v = -100000
		best_move = []
		move_found = False
		board = starting_board[:] 
		for next_move_candidate in range(64):
			if board[next_move_candidate] != 0:
				continue
			legal = attempt_to_make_move_modify(next_move_candidate, board, color,neighbors,  False)
			if legal:
				move_found = True
				game_ended = 0
				g = alphabeta_score(board, how_many_plies_more-1, alpha, beta, -color ,max_player ,game_ended, empties-1)
				board = starting_board[:] 
				if g[0] > v:
					v = g[0]
					best_move = next_move_candidate
				alpha = max(alpha, v)
				if beta <= alpha:        
					break
		if move_found:
			return [v, best_move]
		else:
			game_ended += 1
			v = max(v, alphabeta_score(board, how_many_plies_more, alpha, beta, -color, max_player,game_ended, empties)[0] )
			return [v, best_move ] 
	
	else:
		v = 100000
		best_move = []
		move_found = False
		board = starting_board[:] 
		for next_move_candidate in range(64):
			if board[next_move_candidate] != 0:
				continue
			legal = attempt_to_make_move_modify(next_move_candidate, board, color,neighbors,  False)
			
			if legal:
				move_found = True
				game_ended = 0
			
				g = alphabeta_score(board,how_many_plies_more-1, alpha, beta, -color, max_player,game_ended, empties-1)
				board = starting_board[:] 
				if g[0] < v:
					v = g[0]
					best_move = next_move_candidate
				beta = min(beta, v)
				if beta <= alpha:               
					break
		if move_found:
			return [v, best_move]
		else:
			game_ended += 1
			v = min(v, alphabeta_score(board, how_many_plies_more, alpha, beta, -color, max_player,game_ended, empties)[0] )
			return [v,best_move]

		
neighbors_S = [neighbors_S_function(i,range(64)) for i in range(64)]
neighbors_W = [neighbors_W_function(i,range(64)) for i in range(64)]
neighbors_N = [neighbors_N_function(i,range(64)) for i in range(64)]
neighbors_E = [neighbors_E_function(i,range(64)) for i in range(64)]
neighbors_NE = [neighbors_NE_function(i,range(64)) for i in range(64)]
neighbors_SW = [neighbors_SW_function(i,range(64)) for i in range(64)]
neighbors_NW = [neighbors_NW_function(i,range(64)) for i in range(64)]
neighbors_SE = [neighbors_SE_function(i,range(64)) for i in range(64)]

neighbors = [neighbors_S, neighbors_W, neighbors_N, neighbors_E, neighbors_NE, neighbors_SW, neighbors_NW, neighbors_SE]

for neighbor_group in neighbors:
	for square in range(64):
		current_neighbors = neighbor_group[square]
		while True:
			if len(current_neighbors)<7:
				current_neighbors.append(square)
			else:
				break
			
			
moves_start = list(range(64))
player  = 'X'
opponent = 'O'

board_start = [0 for x in range(64)]

board_start[20] = 1
board_start[27] = 1
board_start[28] = 1
board_start[35] = -1
board_start[36] = 1	

side_board = board_start[:]
reached_the_end = False
range_needed = range(64)

board = board_start
global_node_count = 0
depth = 0
global_game_counter = 0
global_result_list = []
root = Node(board[:], None, -1)
current_node = root

feature_indices = feature_dict.feature_indices
features = feature_dict.features_flat

def calculate_feature(feature, board):
	feature_value = 0
	for piece in feature:
		feature_value = 3*feature_value+board[piece]+1	
	return feature_value
	
def calculate_board_features(board):
	to_return = []
	for feature in features:
		to_return.append( calculate_feature(feature, board) )
	return to_return

def from_symbols_to_numbers(symbol):
	if symbol=='-':
		return 0
	if symbol == 'X':
		return 1
	if symbol == 'O':
		return -1
	
all_files = os.listdir()
all_dict_indices = []
for string in all_files:
	if 'dicts_final_' in string:
		all_dict_indices.append(int(string.replace('dicts_final_', '').replace('.p', '') ) )

latest_dictionary_number = max(all_dict_indices)		
latest_dictionary_filename ='dicts_final_'+  str(latest_dictionary_number)+'.p'
	
	
def move_encoding_string_to_number(string):
	string = string.lower()
	dict_letters = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
	return 8 * ( 8 - int(string[1]) ) + dict_letters[string[0]]
	
def move_encoding_number_to_string(number):
	dict_letters = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h'}
	return dict_letters[number%8] + str(8-number//8)
	
	
global_training_board_list = [ [] for i in range(10) ]
dicts = feature_dict.dicts_flat	
boards_ever_generated = 0		
try:
	dicts = pickle.load(open(latest_dictionary_filename, "rb") )	
except:
	print('dicts_final loading error')
	pass

# try:
	# global_training_board_list = pickle.load(open('global_training_board_list_final.p', "rb") )	
# except:
	# print('global_training_board_list loading error')
	# pass	
	
try:
	current_node = pickle.load(open('current_node.p', "rb") )	
except:
	print('current_node loading error')
	pass	


master_game_record = []	
errors_list_victory = []	
errors_list_points = []
errors_list_bootstrap = []
t0 = time.clock()
time_to_fit = 0.001


killer_move_table = [list(range(64)) for stages in range(64)]
hash_table = [{} for i in range(64)]



play_human_game(board_start[:],-1 )



	
pickle.dump(current_node, open('current_node.p', "wb") )		
pickle.dump(global_training_board_list, open('global_training_board_list_final.p', "wb") )
pickle.dump(boards_ever_generated, open('boards_ever_generated.p', "wb") )	