class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = [True] * n
        left_diagonal = [True] * (2 * n - 1)
        right_diagonal = [True] * (2 * n - 1)
        res = []
        curr = [['.'] * n for i in range(n)]

        def promising(row, col):
            return column[col] and left_diagonal[row + col] and right_diagonal[row - col + n - 1]
        def update_board(row, col, bool):
            column[col] = left_diagonal[row + col] = right_diagonal[row - col + n - 1] = bool
            if bool:
                curr[row][col] = '.'
            else:
                curr[row][col] = 'Q'

        def put_queen(row):
            if row == n:
                res.append([''.join(r) for r in curr])
                return
            for col in range(n):
                if promising(row, col):
                    update_board(row, col, False)
                    put_queen(row + 1)
                    update_board(row, col, True)
        
        put_queen(0)
        
        return res
            

            
    