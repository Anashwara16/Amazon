
# 11. Container With Most Water


class Solution:
    def maxArea(self, height: list[int]) -> int:

        l, r = 0, len(height)-1
        maxArea = 0

        while l < r:

            currentArea = (r-l) * min(height[l], height[r])

            maxArea = max(currentArea, maxArea)

            if height[l] < height[r]:
                l += 1

            else:
                r -= 1

        return maxArea


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    objectNums = Solution()
    print(objectNums.maxArea(height))
