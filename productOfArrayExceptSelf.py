
# 238. Product of Array Except Self


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        array = [0]*len(nums)
        array[0] = 1

        for i in range(1, len(nums)):
            array[i] = array[i-1] * nums[i-1]

        postFix = 1

        for i in reversed(range(len(nums))):
            array[i] = postFix * array[i]
            postFix *= nums[i]

        return array


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    objectNums = Solution()
    print(objectNums.productExceptSelf(nums))
