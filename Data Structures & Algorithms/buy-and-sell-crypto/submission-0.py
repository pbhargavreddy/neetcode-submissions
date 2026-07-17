class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        min_p = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            else:
                maxi = max(maxi,prices[i]-min_p)
        return maxi