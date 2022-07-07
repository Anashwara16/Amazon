
# 334. Increasing Triplet Subsequence


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        if len(nums) < 3:
            return False

        firstSmallestNumber = float('inf')
        secondSmallestNumber = float('inf')

        for n in nums:

            if n <= firstSmallestNumber:
                firstSmallestNumber = n

            elif n <= secondSmallestNumber:
                secondSmallestNumber = n

            else:
                return True

        return False


if __name__ == "__main__":
    nums = [2, 1, 5, 0, 4, 6]
    objectNums = Solution()
    print(objectNums.increasingTriplet(nums))
