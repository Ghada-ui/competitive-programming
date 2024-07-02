class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = [[True for i in range(len(grid[0]))] for j in range(len(grid))]
        count = 0
        def valid_position(row, col):
            return (0 <= col < len(grid[0])) and (0 <= row < len(grid))

        def dfs(grid, row, col, visited):
            nonlocal count

            if grid[row][col]:
                sides = 4

                for x, y in directions:
                    if valid_position(row + x, col + y) and  grid[row + x][col + y]:
                        sides -= 1

                count += sides

            visited[row][col] = False

            for x, y in directions:
                new_row = row + x
                new_col = col + y

                if valid_position(new_row, new_col) and  visited[new_row][new_col]:
                    dfs(grid, new_row, new_col, visited)

        dfs(grid, 0, 0, visited)
        return count
