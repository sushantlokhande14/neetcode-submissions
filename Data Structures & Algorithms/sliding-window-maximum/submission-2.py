class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # bruteforce 

        output = []
        n = len(nums)
        maxi = float("-inf")
        for i in range(n -k + 1 ): 
            maxi = nums[i]
            for j in range(i, i+k): 
                maxi = max(maxi, nums[j])
            output.append(maxi)

        
        return output