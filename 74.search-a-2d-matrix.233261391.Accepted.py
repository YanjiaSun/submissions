








class Solution(object):
    def searchMatrix(self, matrix, target):

        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        while high >= low:
            mid = (high + low) // 2
            value = matrix[mid // cols][mid % cols]
            if target == value:
                return True
            if target > value:
                low = mid + 1
            else:
                high = mid - 1
        return False
