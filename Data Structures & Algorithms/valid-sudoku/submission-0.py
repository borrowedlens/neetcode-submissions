class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_freq = {}
        rows = len(board)
        columns = len(board[0])
        for i in range(rows):
            for j in range(columns):
                if(row_freq.get(board[i][j])):
                    return False
                if(board[i][j] != "."):
                    row_freq[board[i][j]] = 1
            row_freq = {}
        col_freq = {}
        for j in range(columns):
            for i in range(rows):
                if(col_freq.get(board[i][j])):
                    return False
                if(board[i][j] != "."):
                    col_freq[board[i][j]] = 1
            col_freq = {}

        for square in range(9):
            box_freq = {}
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if(box_freq.get(board[row][col])):
                        return False
                    if(board[row][col] != "."):
                        box_freq[board[row][col]] = 1

        return True
        