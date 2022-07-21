
# 169. Majority Element

from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        count = Counter(nums)

        return max(count.keys(), key=count.get)


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    objectNums = Solution()
    print(objectNums.majorityElement(nums))
