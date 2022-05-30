
# 200. Number of Islands

import collections


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                rw, cl = q.popleft()

                directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

                for rdir, cdir in directions:
                    rd, cd = rw + rdir, cl + cdir

                    if (rd in range(rows) and cd in range(cols) and
                            grid[rd][cd] == "1" and (rd, cd) not in visited):
                        q.append((rd, cd))
                        visited.add((rd, cd))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]
    objectNums = Solution()
    print(objectNums.numIslands(grid))
