class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, lowest = 0, math.inf

        for i in prices:
            if i < lowest:
                lowest = i

            max_profit = max(max_profit, i - lowest)

        return max_profit 
