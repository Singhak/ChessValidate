class Utility:

	@classmethod
	def stringToIndexies(cls, value):
		if len(value) == 2:
			return (int(value[0]), int(value[1]))
		else:
			return None
			
			
	# if we have given two position then check those positon are diagonal or not
	@classmethod
	def checkPosAreDiagonal(cls, firstPos, secondPos): #(1,0), (2,1)
	
		if Utility.isStraightMove(firstPos, secondPos):
			return False
		# Here we are caculating the sum and diff beacause
		# 1. Two diagonal positon diff are same Or
		# 2. Two diagonal postion sum are same
		
		diffFirst = abs(firstPos[0] - firstPos[1])
		sumFirst = firstPos[0] + firstPos[1]
		
		diffSecond = abs(secondPos[0] - secondPos[1])
		sumSecond = secondPos[0] + secondPos[1]
		
		if (diffFirst == diffSecond) or (sumFirst == sumSecond):
			return True
		else:
			return False
			
	## Get peice belong to which color
	@classmethod
	def isWhite(cls, pieceType):
		if pieceType[0] == 'W':
			return True
		elif pieceType[0] == 'B':
			return False
		return None
		
		
	@classmethod
	def isStraightMove(cls, fromPos, toPos):
		if (fromPos[0] == toPos[0]) and (fromPos[1] > toPos[1] or fromPos[1] < toPos[1]):
			return True
		if (fromPos[0] > toPos[0] or fromPos[0] < toPos[0]) and (fromPos[1] == toPos[1]):
			return True
		return False
		
	@classmethod
	def printBoard(cls, board):
		print("#############################################")
		for i in range(len(board)):
			for j in range(len(board[0])):
				print(board[i][j], end=" ")
			print()
		print("#############################################")
			
	@classmethod
	def distanceBetweenTwoPositon(cls, fromPos, toPos):
		# This logic of distance valid only for straight and diagonal position 
		# where x and y changed with same value
		
		diffX = abs(fromPos[0] - toPos[0])
		diffY = abs(fromPos[1] - toPos[1])
		
		if diffX == 0 :
			return diffY
		if diffY == 0:
			return diffX
		
	@classmethod
	def isKnightMove(cls, fromPos, toPos):
		diffX = abs(fromPos[0] - toPos[0])
		diffY = abs(fromPos[1] - toPos[1])
		
		if diffX == 1 and diffY == 2:
			return True
		if diffY == 1 and diffX == 2:
			return True
		return False
			
		
		

# print(Utility.checkPosAreDiagonal((5,1), (3,3)))
# print(Utility.checkPosAreDiagonal((5,1), (4,1)))
# input("Press Enter to Exit")
