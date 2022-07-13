
# 695. Max Area of Island


from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            q.append([r, c])
            visited.add((r, c))
            islandArea = 1

            while q:

                qr, qc = q.popleft()

                for dr, dc in directions:
                    row, col = qr + dr, qc + dc

                    if row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] and (row, col) not in visited:
                        q.append([row, col])
                        visited.add((row, col))
                        islandArea += 1

            return islandArea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea


if __name__ == "__main__":
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    objectNums = Solution()
    print(objectNums.maxAreaOfIsland(grid))
