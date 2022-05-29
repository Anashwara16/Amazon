
# 268. Missing Number


class Solution:
    def missingNumber(self, nums):

        n = len(nums)

        totalSum = n(n+1)/2

        actualSum = sum(nums)

        return (totalSum - actualSum)


if __name__ == "__main__":
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    objectNums = Solution()
    print(objectNums.missingNumber(nums))
