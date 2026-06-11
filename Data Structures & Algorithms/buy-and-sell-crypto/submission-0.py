class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        minValuePointer = 0

        for i in range(len(prices)):
            if prices[i] < prices[minValuePointer]:
                minValuePointer = i
            elif prices[i] - prices[minValuePointer] > currMax:
                currMax = prices[i] - prices[minValuePointer]

        return currMax
        
        