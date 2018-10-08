# A western chess game with built-in chess AI coded in Python.

Techniques used in chess code:

1.	Bit flags are use to conveniently identify chess pieces in the code.

	For example, assume each chess piece is identified by a unique ID. To correctly identify if a chess piece is a "rook", as there are 4 rooks in the chess, you need to check if its ID is one of the IDs of the 4 rooks. This means 4 comparisons will need to be done.

	However, using bit flags, the information can be stored in each bit. Assume a 3 bits binary number is used, the 1st bit defines if the piece is white(0) or black(1), the 2nd bit defines if the piece is in left(0) or right(1) position, and the 3rd bit defines if the piece is not a rook(0) or is a rook(1), i.e. the binary number 101 means a chess piece that is a black, left rook. Then simly checking the 3rd bit can tell us if the piece is a rook or not, as compared to using 4 comparisons.

Techniques used in chess AI:

1.	A cost function is used to calculate how good the overall situation of the current board positions are. For example, the fewer
	the opponent chess pieces are left on the board, the lower the cost. The goal for the AI is to minimize the cost as much as possible.

2.	Recurrsion is used so the AI can calculate the cost of the next possible moves.

3.	Minimax value is calculated. That is, the AI will only take opponent moves that lead to the most disadvantage situation into 
	consideration. And it will try to find the most advantageous move from the most disadvantageous situation.