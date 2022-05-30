
# 16. 3Sum Closest


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        diff = float('inf')
        nums.sort()

        for i in range(len(nums)):

            lo, hi = i+1, len(nums)-1

            while lo < hi:

                threeSumClosest = nums[i] + nums[lo] + nums[hi]

                if abs(target - threeSumClosest) < abs(diff):
                    diff = target - threeSumClosest

                if threeSumClosest < target:
                    lo += 1

                else:
                    hi -= 1

                if diff == 0:
                    break

        return target - diff


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    objectNums = Solution()
    print(objectNums.threeSumClosest(nums, target))
