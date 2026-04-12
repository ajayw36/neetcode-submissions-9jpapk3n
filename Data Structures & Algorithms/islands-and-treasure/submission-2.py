# multi source bfs

from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        dq = deque()

        def add_cell(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c))
            dq.append([r, c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dq.append([r, c])
                    visited.add((r, c))
        
        dist = 0
        while dq:
            for i in range(len(dq)):
                r, c = dq.popleft()
                grid[r][c] = dist
                add_cell(r + 1, c)
                add_cell(r - 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)
            dist += 1
        

            
