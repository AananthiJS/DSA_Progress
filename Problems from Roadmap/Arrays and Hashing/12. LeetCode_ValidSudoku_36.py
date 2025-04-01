from collections import defaultdict

board = [["5","9",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

class Solution:
    def isValidSudoku(self, board):
        column = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in row[r] or
                    board[r][c] in column[c] or
                    board[r][c] in square[(r//3, c//3)]):
                    return False
                column[c].add(board[r][c])
                row[r].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True
    
obj = Solution()
print(obj.isValidSudoku(board))