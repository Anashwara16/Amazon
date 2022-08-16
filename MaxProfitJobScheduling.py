
# 1235. Maximum Profit in Job Scheduling


from bisect import bisect, bisect_left


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:

        n = len(startTime)

        jobs = sorted(list(zip(startTime, endTime, profit)))
        print(jobs)

        startTimings = [jobs[i][0] for i in range(n)]
        print(startTimings)

        def dp(i):

            if i == n:
                return 0

            maxProfit = dp(i+1)

            j = bisect_left(startTimings, jobs[i][1])
            print("i, j => ", i, j)

            maxProfit = max(maxProfit, dp(j) + jobs[i][2])
            print("MAXPROFIT =>", maxProfit)

            return maxProfit

        return dp(0)


if __name__ == "__main__":
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    objNums = Solution()
    print(objNums.jobScheduling(startTime, endTime, profit))
