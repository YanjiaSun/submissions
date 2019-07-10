








class Solution(object):
    def minPathSum(self, grid):

        m = len(grid)
        n = len(grid[0])
        min_path = [float('inf') for _ in range(n + 1)]
        min_path[1] = 0
        for row in range(1, m + 1):
            new_min_path = [float('inf') for _ in range(n + 1)]
            for col in range(1, n + 1):
                new_min_path[col] = grid[row - 1][col - 1] + min(min_path[col], new_min_path[col - 1])
            min_path = new_min_path
        return min_path[-1]
