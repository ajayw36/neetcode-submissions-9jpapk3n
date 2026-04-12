from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        res = [[float('inf')]*cols for _ in range(rows)]
        def bfs(i, j):
            count = 0
            visited = [[False]*cols for _ in range(rows)]
            dq = deque()
            dq.append([i, j])
            visited[i][j] = True
            while dq:
                for _ in range(len(dq)):
                    c = dq.popleft()
                    x, y = c[0], c[1]
                    if grid[x][y] == 0:
                        return count
                    if x + 1 < rows and grid[x+1][y] != -1 and not visited[x+1][y]:
                        dq.append([x+1, y])
                        visited[x+1][y] = True
                    if y + 1 < cols and grid[x][y+1] != -1 and not visited[x][y+1]:
                        dq.append([x, y+1])
                        visited[x][y+1] = True
                    if x - 1 >= 0 and grid[x-1][y] != -1 and not visited[x-1][y]:
                        dq.append([x-1, y])
                        visited[x-1][y] = True
                    if y - 1 >= 0 and grid[x][y-1] != -1 and not visited[x][y-1]:
                        dq.append([x, y-1])
                        visited[x][y-1] = True
                count += 1
            return float('inf')

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == -1:
                    res[i][j] = -1
                else:
                    res[i][j] = bfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = res[i][j]
