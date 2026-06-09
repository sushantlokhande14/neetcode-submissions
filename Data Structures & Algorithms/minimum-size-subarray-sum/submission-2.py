class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        L = 0 
        total = 0 
        minLength = float('inf')


        for R in range(len(nums)): 

            total += nums[R]

            while total >= target: 

                minLength = min(minLength, R- L + 1)
                total -= nums[L]
                L +=1 

        if minLength == float('inf'): 
            return 0 
        
        else: 
            return minLength 