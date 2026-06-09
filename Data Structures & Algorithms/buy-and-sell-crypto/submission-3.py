class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0 
        n = len(prices)

        for i in range(n): 
            for j in range(i+1 , n ): 
                prof = prices[j] - prices[i]

                maxProf = max(prof, maxProf)
        
        return maxProf