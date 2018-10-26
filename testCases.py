#Test case for chess move validation

import Chess

board = [['WR', "WH", "WB", "WQ", "WK", "WB", "WH", "WR"],
		['WP', "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
		["--", "--", "--", "--", "--", "--", "--", "--"],
		["--", "--", "--", "--", "--", "--", "--", "--"],
		["--", "--", "BP", "--", "--", "--", "--", "--"],
		["--", "--", "--", "--", "--", "--", "--", "--"],
		['BP', "BP", "--", "BP", "BP", "BP", "BP", "BP"],	
		['BR', "BH", "BB", "BQ", "BK", "BB", "BH", "BR"]]	
chess = Chess.Chess()
chess.setBoardPosition(board)

#case 1 

print("\n\tBP","63", "43\n")
chess.makeMove("BP","63", "43") #valid
print("\n\tBP","64", "45\n")
chess.makeMove("BP","64", "45") #invalid
print("\n\tBP","65", "46\n")
chess.makeMove("BP","65", "46") #invalid
print("\n\tBP","66", "55\n")
chess.makeMove("BP","66", "55") #invalid
print("\n\tBP","66", "65\n")
chess.makeMove("BP","66", "65") #invalid
print("\n\tBP","42", "52\n")
chess.makeMove("BP","42", "52") #invalid9



#case 2 Black Pawn 1-step
#case 3 Black Pawn diagonal-step


board = [['WR', "WH", "WB", "WQ", "WK", "WB", "WH", "WR"],
		['WP', "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
		["--", "--", "--", "--", "--", "--", "--", "--"],
		["--", "--", "--", "--", "--", "--", "--", "--"],
		["--", "--", "--", "--", "--", "--", "--", "--"],
		["--", "--", "--", "--", "--", "--", "--", "--"],
		['BP', "BP", "BP", "BP", "BP", "BP", "BP", "BP"],	
		['BR', "BH", "BB", "BQ", "BK", "BB", "BH", "BR"]]
input("Press Enter to Exit")