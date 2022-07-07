# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longestStreak = 0
        numSet = set(nums)

        for num in numSet:

            if num-1 not in numSet:
                currentNum = num
                currentStreak = 1

                while currentNum+1 in numSet:
                    currentNum += 1
                    currentStreak += 1

                longestStreak = max(longestStreak, currentStreak)

        return longestStreak


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    objectNums = Solution()
    print(objectNums.longestConsecutive(nums))
