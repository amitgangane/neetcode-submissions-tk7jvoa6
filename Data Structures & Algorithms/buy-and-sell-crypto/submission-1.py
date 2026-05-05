class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i= 0
        j = 1
        n = len(prices)-1
        max_return = 0
        while j<len(prices):
            if prices[i] > prices[j]:
                i=j
            
            price = prices[j]-prices[i]
            max_return = max(max_return, price)
            j +=1

        return max_return