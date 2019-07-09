_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zero = any([True for c in range(cols) if matrix[0][c] == 0])
        first_col_zero = any([True for r in range(rows) if matrix[r][0] == 0])
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
        if first_row_zero:
            matrix[0] = [0] * cols
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0