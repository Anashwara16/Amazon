
# 1730. Shortest Path to Get Food

from collections import deque


class Solution:
    def getFood(self, grid: list[list[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        personRow, personCol = 0, 0

        def findPerson(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == "X" or (r, c) in visited:
                return
            visited.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "#":
                    q.append([r, c])
                    visited.add((r, c))
                if grid[r][c] == "*":
                    personRow, personCol = r, c

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        steps = 0

        while q:

            for i in range(len(q)):

                qr, qc = q.popleft()

                grid[qr][qc] = steps

                if qr == personRow and qc == personCol:
                    return grid[qr][qc]

                for dr, dc in directions:
                    row, col = qr + dr, qc + dc
                    findPerson(row, col)

            steps += 1

        return -1


if __name__ == "__main__":
    # grid = [["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "*", "O", "X", "O", "#", "O", "X"], ["X", "O", "O",

    # grid = [["X", "X", "X", "X", "X"], ["X", "*", "X", "O", "X"],
            # ["X", "O", "X", "#", "X"], ["X", "X", "X", "X", "X"]]

    grid = [["X", "X", "X", "X", "X", "X"], ["X", "*", "O", "O", "O", "X"],
            ["X", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X"]]

    objectNums = Solution()
    print(objectNums.getFood(grid))
