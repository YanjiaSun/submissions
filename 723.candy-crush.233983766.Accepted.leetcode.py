class Solution(object):
    def candyCrush(self, board):
        rows, cols = len(board), len(board[0])
        while True:
            stable = True
            to_crush = [[False for _ in range(cols)] for _ in range(rows)]
            for c in range(cols):
                for r in range(rows):
                    if r < rows - 2 and board[r][c] == board[r + 1][c] == board[r + 2][c] and board[r][c] != 0:
                        to_crush[r][c] = to_crush[r + 1][c] = to_crush[r + 2][c] = True
                        stable = False
                    if c < cols - 2 and board[r][c] == board[r][c + 1] == board[r][c + 2] and board[r][c] != 0:
                        to_crush[r][c] = to_crush[r][c + 1] = to_crush[r][c + 2] = True
                        stable = False
            if stable:
                return board
            for c in range(cols):
                new_col = [0 for _ in range(rows)]
                new_r = rows - 1
                for r in range(rows - 1, -1, -1):
                    if not to_crush[r][c]:
                        new_col[new_r] = board[r][c]
                        new_r -= 1
                if new_r != -1:
                    for r in range(rows):
                        board[r][c] = new_col[r]
