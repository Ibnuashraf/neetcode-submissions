class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                if (prices[j]-prices[i])>diff:
                    diff=prices[j]-prices[i]
                else:
                    pass
        return diff
                
            

        