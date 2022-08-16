# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque


def solution(K, A):
    # write your code in Python 3.6
    rows, cols = len(A), len(A[0])
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    houses = set()
    noOfHouses = 0
    result = 0
    count = [[0 for _ in range(cols)] for _ in range(rows)]

    def bfs(r, c, K):

        q = deque()
        q.append([r, c, K])
        visited = set()

        while q:
            for i in range(len(q)):
                qr, qc, qk = q.popleft()

                if (qr, qc) not in visited:
                    visited.add((qr, qc))
                    count[qr][qc] += 1

                for dr, dc in directions:
                    row, col, kcount = (qr + dr), (qc + dc), (qk-1)

                    if (0 <= row < rows) and (0 <= col < cols) and kcount >= 0 and (row, col) not in visited:
                        q.append([row, col, kcount])

    for r in range(rows):
        for c in range(cols):
            if A[r][c] == 1:
                noOfHouses += 1
                bfs(r, c, K)
                houses.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if count[r][c] == noOfHouses and (r, c) not in houses:
                result += 1

    return result
