
# 42. Trapping Rain Water


class Solution:
    def trap(self, height: list[int]) -> int:

        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]

        water = 0

        while left < right:

            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]

            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]

        return water


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    objectNums = Solution()
    print(objectNums.trap(height))
