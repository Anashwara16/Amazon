
# 733. Flood Fill


from tracemalloc import start


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:

        rows, cols = len(image), len(image[0])
        visited = set()

        def dfs(r, c, oldColor, newColor):
            if r < 0 or r == rows or c < 0 or c == cols or image[r][c] != oldColor or image[r][c] in visited:
                return

            visited.add((r, c))
            image[r][c] = newColor
            dfs(r+1, c, oldColor, newColor)
            dfs(r-1, c, oldColor, newColor)
            dfs(r, c+1, oldColor, newColor)
            dfs(r, c-1, oldColor, newColor)

        startingColor = image[sr][sc]

        if startingColor == newColor:
            return image

        dfs(sr, sc, startingColor, newColor)

        return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    objectNums = Solution()
    print(objectNums.floodFill(image, sr, sc, color))
