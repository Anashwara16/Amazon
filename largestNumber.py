

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_subarray = current_subarray = nums[0]

        for num in nums[1:]:
            current_subarray = max(num, current_subarray+num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    objectNums = Solution()
    print(objectNums.maxSubArray(nums))
