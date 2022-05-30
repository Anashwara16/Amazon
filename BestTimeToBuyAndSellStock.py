
# 121. Best Time to Buy and Sell Stock


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        minimumPrice = float('inf')
        maximumProfit = 0

        for i in range(len(prices)):

            if prices[i] < minimumPrice:
                minimumPrice = prices[i]

            elif (prices[i] - minimumPrice) > maximumProfit:
                maximumProfit = prices[i] - minimumPrice

        return maximumProfit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    objectNums = Solution()
    print(objectNums.maxProfit(prices))
