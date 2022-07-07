
# 1197. Minimum Knight Moves


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def bfs(x, y):

            visited = set()
            queue = deque([(0, 0)])
            moves = 0

            while queue:
                currentLevel = len(queue)

                for i in range(currentLevel):

                    currentX, currentY = queue.popleft()

                    if (currentX, currentY) == (x, y):
                        return moves

                    for offsetX, offsetY in offsets:

                        nextX, nextY = currentX + offsetX, currentY + offsetY

                        if (nextX, nextY) not in visited:
                            visited.add((nextX, nextY))
                            queue.append((nextX, nextY))

                moves += 1

        return bfs(x, y)


if __name__ == "__main__":
    x = 2
    y = 1
    objectNums = Solution()
    print(objectNums.minKnightMoves(x, y))
