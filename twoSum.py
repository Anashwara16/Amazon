
# 1. Two Sum


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        indices = []
        hashmap = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hashmap:
                return [i, hashmap[complement]]

            hashmap[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    objectNums = Solution()
    print(objectNums.twoSum(nums, target))
