class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        freqOfItems = [0] * 2
        
        for i in range(3):
            
            freqOfItems[0] += board[i].count("X")
            freqOfItems[1] += board[i].count("O")
            
        winner = self.checkWinner(board) #-1 - invalid, 0 - X won, 1 - O won, 2 - draw, 
        
        #check diff of X and O
        if 0 <= freqOfItems[0] - freqOfItems[1] <= 1:
            if (winner == 0 and freqOfItems[0] - freqOfItems[1] != 1) or (winner == 1 and freqOfItems[0] - freqOfItems[1] != 0):
                return False
            elif winner == -1:
                return False
            else:
                return True
        else:
            return False
            
        

    def checkWinner(self, board):
        winnerCount = [0] * 2 #[0] for X, [1] for O
        
        #row wise
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
            winnerCount[0] += 1

        if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
            winnerCount[1] += 1
        
        #column wise
        if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
            winnerCount[0] += 1

        if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
            winnerCount[1] += 1

        #diganoal wise
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            winnerCount[0] += 1

        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            winnerCount[1] += 1

        if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
            winnerCount[0] += 1

        if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
            winnerCount[1] += 1

        #check winner validity, and also X winning pattern can occur twice
        if winnerCount[0] > 2 or winnerCount[1] > 1 or (winnerCount[0] != 0 and winnerCount[1] != 0 and winnerCount[0] == winderCount[1]):
            return -1

        elif 1 <= winnerCount[0] <= 2 and winnerCount[1] == 0:
            return 0
        
        elif winnerCount[1] == 1 and winnerCount[0] == 0:
            return 1
        
        #draw
        return 2

        

