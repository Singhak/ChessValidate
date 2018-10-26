# Chess Library
from Utility import *
 
class Chess:
	# def __init__(self, board):
		# self.board = board #create board
	
	def setBoardPosition(self, board):
		self.board = board
	
	## This function is point of interaction for any type of chess movement
	def makeMove(self, pieceType, posFrom, posTo):
		_from = Utility.stringToIndexies(posFrom)
		_to = Utility.stringToIndexies(posTo)
		isValid = False
		if pieceType[1] == 'P':
			isValid = self.pawnMove(pieceType, _from, _to)
		if pieceType[1] == 'Q':
			isValid = self.queenMove(pieceType, _from, _to)
		if pieceType[1] == 'R':
			isValid = self.rookMove(pieceType, _from, _to)
		if pieceType[1] == 'H':
			isValid = self.knightMove(pieceType, _from, _to)
		if pieceType[1] == 'K':
			isValid = self.kingMove(pieceType, _from, _to)
		if pieceType[1] == 'B':
			isValid = self.bishopsMove(pieceType, _from, _to)
			
		## If move is valid then make move
		if isValid:
			self.doMove(pieceType, _from, _to)
		
		
	####################################
	
	def knightMove(self, pieceType, posFrom, posTo):
	
		if Utility.checkPosAreDiagonal(posFrom, posTo):
			print(pieceType, "Cannot make diagonal position move")
			return False
		if Utility.isStraightMove(posFrom, posTo):
			print(pieceType, "Cannot make straight position move")
			return False
			
		if not self.isValidMove(pieceType, posFrom, posTo):
			return False
		
		if not Utility.isKnightMove(posFrom, posTo):
			print(pieceType, "movement is not valid")
			return False
		
		return True
				
		
	######################## Queen Move ################################
	
	def queenMove(self, pieceType, posFrom, posTo):

		if not Utility.checkPosAreDiagonal(posFrom, posTo) or not Utility.isStraightMove(posFrom, posTo):
			print(pieceType, "Cannot make move other than diagonal or straight  position")
			return False
		if not self.isValidMove(pieceType, posFrom, posTo):
			return False
			
			
		return True
			
	######################## Pawn ################################
	
	def pawnMove(self, pieceType, posFrom, posTo):

		if not self.isValidMove(pieceType, posFrom, posTo):
			return False
		
		if Utility.checkPosAreDiagonal(posFrom, posTo) and self.posIsEmpty(posTo):
			print("Pawn Cannot make move on empty diagonal position")
			return False
			
		if not Utility.checkPosAreDiagonal(posFrom, posTo) and not self.posIsEmpty(posTo):
			print("Pawn Cannot make straight move on non-empty position")
			return False
			
		## Conditon check for pawn back movement
		isWhite = Utility.isWhite(pieceType)
		if (isWhite and posTo[0] < posFrom[0]) or (not isWhite and posTo[0] > posFrom[0]):
			print("Pawn cannot move back")
			return False
			
		if Utility.distanceBetweenTwoPositon(posFrom, posTo) != 1 and not self.isPeiceOnBaseLoc(pieceType, posFrom):
			print("Pawn cannot move than one step from given position")
			return False
			
		if self.isPeiceOnBaseLoc(pieceType, posFrom):
			if Utility.distanceBetweenTwoPositon(posFrom, posTo) == 2 and not self.posIsEmpty(posTo):
				print("Pawn cannot move from given position")
				return False
			elif Utility.distanceBetweenTwoPositon(posFrom, posTo) > 2:
				print("Pawn cannot move more than one or two step from base location")
			
		return True
			
	######################## Rook ################################
		
	def rookMove(self, pieceType, posFrom, posTo):	
	
		if Utility.checkPosAreDiagonal(posFrom, posTo):
			print(pieceType, "Cannot move random position")
			return False
			
		if not self.isValidMove(pieceType, posFrom, posTo):
			return False
			
		return True
		
		
	######################## Bishops ################################
	
	def bishopsMove(self, pieceType, posFrom, posTo):
		if not Utility.checkPosAreDiagonal(posFrom, posTo):
			print(pieceType, "Cannot move straight position")
			return False
			
		if not self.isValidMove(pieceType, posFrom, posTo):
			return False
		
		return True
		
	######################## King ################################
	
	def kingMove(pieceType, posFrom, posTo):
		if not self.isValidMove(pieceType, posFrom, posTo):
			return False
		if Utility.distanceBetweenTwoPositon(posFrom, posTo) != 1:
			return False
			
		return True
	
	def doMove(self, pieceType, fromPos, toPos):
		self.board[fromPos[0]][fromPos[1]] = "--"
		self.board[toPos[0]][toPos[1]] = pieceType
		Utility.printBoard(self.board)
		
	################################################
	# Check is given peice at Base Location or not #
	################################################
	def isPeiceOnBaseLoc(self, pieceType, fromPos):
		if pieceType == 'WP' and fromPos[0] == 1:
			return True
		elif pieceType[0] == 'W' and fromPos[0] == 0:
			return True
		if pieceType == 'BP' and fromPos[0] == 6:
			return True
		elif pieceType[0] == 'B' and fromPos[0] == 7:
			return True
		return False
		
	
	##########################################
	# Checking is empty space at given space #
	##########################################
	def posIsEmpty(self, pos):
		if self.board[pos[0]][pos[1]] == "--":
			return True
		else:
			return False
	
	##########################################################
	# Checking is some common move validation at given space #
	##########################################################
	def isValidMove(self, pieceType, fromPos, toPos):
		if self.posIsEmpty(fromPos):
			print("Cannot move empty peice")
			return False
		if toPos[0] < 0 or toPos[1] < 0:
			print(pieceType, "cannot move since Destination position cannot be negative")
			return False
			
		if toPos[0] > 7 or toPos[1] > 7:
			print(pieceType, "cannot move since Destination Position is out of board")
			return False
			
		if Utility.isWhite(pieceType) == Utility.isWhite(self.getPeiceAt(toPos)):
			print(pieceType, "Cannot make move since same color peice at destination")
			return False

		if pieceType[1] != 'H' and ( self.IsPieceInBtwMoves(fromPos, toPos) or Utility.isKnightMove(fromPos, toPos)):
			print(pieceType,"Cannot jump over the peice")
			return False
		
		return True
			
	###################################################################
	# In this method we  checking that, is there any peice in between #
	# the from and to position										  #
	###################################################################
	def IsPieceInBtwMoves(self, fromPos, toPos):
		i = j = 0
	
		if fromPos[0] > toPos[0]:
				i = -1
		if fromPos[0] < toPos[0]:
				i = 1
				
		if fromPos[1] > toPos[1]:
				j = -1
		if fromPos[1] < toPos[1]:
				j = 1
			
		x = fromPos[0] + i
		y = fromPos[1] + j
		
		# we travese each each postion till they reached in target position or till any non-empty peice found in between
		while x != toPos[0] or y != toPos[1]: 
			if not self.posIsEmpty((x,y)):
				return True
			if x != toPos[0]:
				x += i
			if y != toPos[1]:
				y += j
				
		return False
		
	######################################
	#  Get peice name at given position  #
	######################################
	def getPeiceAt(self, pos):
		return self.board[pos[0]][pos[1]]