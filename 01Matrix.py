
# 542. 01 Matrix

from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:

        rows, cols = len(mat), len(mat[0])
        q = deque()
        visited = set()

        def checkZeros(r, c):
            if (r < 0) or (r == rows) or (c < 0) or (c == cols) or mat[r][c] == 0 or (r, c) in visited:
                return

            q.append([r, c])
            visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        distance = 0

        while q:

            for i in range(len(q)):

                qr, qc = q.popleft()
                mat[qr][qc] = distance
                for dr, dc in directions:
                    row, col = qr + dr, qc + dc
                    checkZeros(row, col)

            distance += 1

        return mat


if __name__ == "__main__":
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    objectNums = Solution()
    print(objectNums.updateMatrix(mat))
