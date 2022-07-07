
# 55. Jump Game

class Solution:
    def canJump(self, nums: list[int]) -> bool:

        goal = len(nums)-1

        for i in range(len(nums)-1, -1, -1): 
            if i + nums[i] >= goal: 
                goal = i

        return True if goal == 0 else False


if __name__ == "__main__":
    nums = [9, 4, 2, 1, 0, 2, 0]
    objectNums = Solution()
    print(objectNums.canJump(nums))