
# 289. Game of Life


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:

        rows, cols = len(board), len(board[0])

        print("BEFORE ==> ", board)

        def countNeighbors(r, c):
            nei = 0

            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i == rows or j == cols):
                        continue

                    if board[i][j] in [1, 3]:
                        print("Either 1 or 3 --", board[i][j])
                        print("STATE OF BOARD ==> ", board)
                        nei += 1

            return nei

        for r in range(rows):
            for c in range(cols):

                nei = countNeighbors(r, c)

                if board[r][c]:
                    if nei in [2, 3]:
                        board[r][c] = 3
                else:
                    if nei == 3:
                        board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    board[r][c] = 0
                if board[r][c] in [2, 3]:
                    board[r][c] = 1

        print("AFTER ==> ", board)


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    objectNums = Solution()
    print(objectNums.gameOfLife(board))
