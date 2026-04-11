class Solution:
    def totalNQueens(self, n: int) -> int:
        column = [True] * n
        left_diagonal = [True] * (n * 2 - 1)
        right_diagonal = [True] * (n * 2 - 1)
        def update_board(row, col, remove):
            left_diagonal[row + col] = right_diagonal[row - col + n - 1] = column[col] = remove
        def promising(row, col):
            return left_diagonal[row + col] and right_diagonal[row - col + n - 1] and column[col]
        def put_queen(row):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if promising(row, col):
                    update_board(row, col, False)
                    count += put_queen(row+1)
                    update_board(row, col, True)
            return count
        return put_queen(0)

