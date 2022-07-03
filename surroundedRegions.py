
# 130. Surrounded Regions


class Solution:
    def solve(self, board: list[list[str]]) -> list[list[str]]:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O"):
                return

            board[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)

        for r in rows:
            for c in cols:
                if (board[r][c] == "O") and (r in [0, rows-1] or c in [0, cols-1]):
                    capture(r, c)

        for r in rows:
            for c in cols:
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in rows:
            for c in cols:
                if board[r][c] == "T":
                    board[r][c] = "O"

        return board


if __name__ == "__main__":
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    objectNums = Solution()
    print(objectNums.solve(board))
