class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf') 
        maxprof = 0
        for price in prices:
            #get value
            
            minprice = min(minprice, price)
            
            maxprof = max(maxprof, price - minprice)
        return maxprof 
        
