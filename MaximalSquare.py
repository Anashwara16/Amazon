
# 221. Maximal Square


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def getMaxArea(r, c):

            if r >= rows or c >= cols:
                return 0

            if (r, c) not in cache:
                right = getMaxArea(r, c + 1)
                down = getMaxArea(r + 1, c)
                diagonal = getMaxArea(r + 1, c + 1)

                cache[(r, c)] = 0

                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(right, diagonal, down)

            return cache[(r, c)]

        getMaxArea(0, 0)

        side = max(cache.values())
        maxAreaSquare = side**2

        return maxAreaSquare


if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    objectNums = Solution()
    print(objectNums.maximalSquare(matrix))
