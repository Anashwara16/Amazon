
# 75. Sort Colors


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        current, left, right = 0, 0, len(nums)-1

        while current <= right:

            if nums[current] == 0:
                nums[current], nums[left] = nums[left], nums[current]
                left += 1

            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
                current -= 1

            current += 1

        return nums


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    objectNums = Solution()
    print(objectNums.sortColors(nums))
