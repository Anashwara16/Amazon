
# 300. Longest Increasing Subsequence


import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        sub = []

        for num in nums:

            i = bisect.bisect_left(sub, num)

            if i == len(sub):
                sub.append(num)

            else:
                sub[i] = num

        return len(sub)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    objectNums = Solution()
    print(objectNums.lengthOfLIS(nums))
