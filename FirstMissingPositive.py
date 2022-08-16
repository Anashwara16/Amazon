
# 41. First Missing Positive


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(n):

            val = abs(nums[i])

            if val in range(1, n+1):

                if nums[val-1] > 0:
                    nums[val-1] *= (-1)

                elif nums[val-1] == 0:
                    nums[val-1] = (-1)*(n+1)

        for i in range(1, n+1):
            if nums[i-1] >= 0:
                return i

        return (n+1)


if __name__ == "__main__":
    nums = [7, 8, 9, 11, 12]
    objectNums = Solution()
    print(objectNums.firstMissingPositive(nums))
