
# 239. Sliding Window Maximum

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        q = deque()
        l = r = 0
        output = []

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            print(q)

            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                print(output)
                l += 1

            r += 1

        return output


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    objectNums = Solution()
    print(objectNums.maxSlidingWindow(nums, k))
