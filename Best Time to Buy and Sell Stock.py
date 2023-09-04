class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        x = 0
        y = prices[0]       
        for i in prices: 
            x = max(x, i - y)
            y = min(y, i)
        return(x)
