
# 1130. Minimum Cost Tree From Leaf Values


from functools import lru_cache


class Solution:
    def countArrangement(self, N: int) -> int:
        # backtracking -> dp
        res = 0
        nums = tuple(range(1, N+1))
        print(nums)

        @lru_cache(None)
        def dfs(nums, i):
            if i == N+1:  # to the end
                return 1
            res = 0
            for j, num in enumerate(nums):
                if not num % i or not i % num:
                    print(num % i, i % num)
                    print(tuple(nums[:j] + nums[j+1:]))
                    res += dfs(tuple(nums[:j] + nums[j+1:]), i+1)
            return res

        return dfs(nums, 1)


if __name__ == "__main__":
    n = 5
    objectNums = Solution()
    print(objectNums.countArrangement(n))
