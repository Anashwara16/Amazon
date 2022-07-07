# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        lengthOfNums = len(nums)
        array = [0]*lengthOfNums

        array[0] = 1

        for i in range(1, lengthOfNums):
            array[i] = nums[i-1] * array[i-1]

        postFix = 1

        for i in reversed(range(lengthOfNums)):
            array[i] = postFix * array[i]
            postFix *= nums[i]

        return array


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    objectNums = Solution()
    print(objectNums.productExceptSelf(nums))
