
# 198. House Robber


class Solution:

    def rob(self, nums: list[int]) -> int:

        # Special handling for empty case.
        if not nums:
            return 0

        rob1, rob2 = 0, 0

        for n in nums:
            currentMax = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = currentMax

        return rob2


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    objectNums = Solution()
    print(objectNums.rob(nums))
