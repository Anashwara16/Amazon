
# 31. Next Permutation


class Solution:
    def nextPermutation(self, nums: list[int]):

        i = j = l = len(nums)-1

        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i > 0:

            while nums[j] <= nums[i-1]:
                j -= 1

            nums[i-1], nums[j] = nums[j], nums[i-1]

            nums[i: l+1] = nums[i:l+1][::-1]

        if i == 0:
            nums.reverse()

        return nums


if __name__ == "__main__":
    nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    objectNums = Solution()
    print(objectNums.nextPermutation(nums))
