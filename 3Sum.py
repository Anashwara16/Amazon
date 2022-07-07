
# 15. 3Sum


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        result = []
        nums.sort()

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i+1, len(nums)-1

            while lo < hi:

                threeSum = nums[i] + nums[lo] + nums[hi]

                if threeSum < 0:
                    lo += 1

                elif threeSum > 0:
                    hi -= 1

                else:
                    result.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1

        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    objectNums = Solution()
    print(objectNums.threeSum(nums))
