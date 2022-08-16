
from collections import deque


class Solution:

    def stores(self, K, A):
        rows, cols = len(A), len(A[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        houses = set()
        noOfHouses = 0
        distance = 0
        result = 0
        count = [[0 for _ in range(cols)] for _ in range(rows)]
        q = deque()
        visited = set()

        def bfs(r, c):
            if (r < 0) or (r == rows) or (c < 0) or (c == cols) or A[r][c] != 0 or (r, c) in visited or (r, c) in houses:
                return

            q.append([r, c])
            visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if A[r][c] == 1:
                    noOfHouses += 1
                    q.append([r, c])
                    houses.add((r, c))
                    visited.add((r, c))

        while q:
            for i in range(len(q)):
                qr, qc = q.popleft()
                count[qr][qc] = distance

                for dr, dc in directions:
                    row, col = (qr + dr), (qc + dc)
                    bfs(row, col)

            distance += 1

        print(count)

        for r in range(rows):
            for c in range(cols):
                if count[r][c] <= K and (r, c) not in houses:
                    result += 1

        return result


if __name__ == "__main__":
    K = 2
    A = [[0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]]
    objectNums = Solution()
    print(objectNums.stores(K, A))
