
# 875. Koko Eating Bananas


from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        l = 1
        r = max(piles)
        result = r

        while l <= r:

            mid = (l+r)//2
            total = 0

            for p in piles:
                total += ceil(p/mid)

            if total <= h:
                result = min(result, mid)
                r = mid - 1

            else:
                l = mid + 1

        return result


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    objectNums = Solution()
    print(objectNums.minEatingSpeed(piles, h))
