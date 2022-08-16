
# 1488. Avoid Flood in The City

from collections import Counter, defaultdict


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:

        ans = [-1 for _ in range(len(rains))]
        rain = Counter()
        zeroCount = 0
        zeroIndex = 0

        for i, r in enumerate(rains):

            if r != 0:
                rain[r] = 1 + rain.get(r, 0)
                rain[rains[zeroIndex]] = 1 + rain.get(rains[zeroIndex], 0)

            elif r == 0:
                zeroCount += 1
                rc = rain.most_common(1)
                if rc:
                    sub = rc[0][0]
                    ans[i] = sub
                    rain[sub] -= 1
                    zeroIndex = i
                else:
                    ans[i] = 1
                if rain[sub] <= 0:
                    del rain[sub]

        print(rain)

        '''
        maxRain = max(rain.values())
        if maxRain > 1:
            return []
        '''
        return ans


if __name__ == "__main__":
    #rains = [1, 2, 3, 4]
    rains = [1, 2, 0, 0, 1, 2]
    print("Rain => ", rains[:-2])
    #rains = [1, 2, 0, 1, 2]
    #rains = [69, 0, 0, 0, 69]
    #rains = [1, 1, 0, 0]
    objectNums = Solution()
    print(objectNums.avoidFlood(rains))
