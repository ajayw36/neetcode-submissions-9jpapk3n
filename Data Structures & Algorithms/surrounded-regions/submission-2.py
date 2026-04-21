class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        stack = []
        for j in range(m):
            if board[0][j] == 'O':
                board[0][j] = 'S'
                stack.append((0, j))
            if board[n - 1][j] == 'O':
                board[n - 1][j] = 'S'
                stack.append((n - 1, j))
        for i in range(1, n - 1):
            if board[i][0] == 'O':
                board[i][0] = 'S'
                stack.append((i, 0))
            if board[i][m - 1] == 'O':
                board[i][m - 1] = 'S'
                stack.append((i, m - 1))
        
        while stack:
            curr = stack.pop()
            i, j = curr
            for di, dj in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + di < n and 0 <= j + dj < m and board[i + di][j + dj] == 'O':
                    board[i + di][j + dj] = 'S'
                    stack.append((i + di, j + dj))

        for i in range(n):
            for j in range(m):
                if board[i][j] != 'S':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

        
        
