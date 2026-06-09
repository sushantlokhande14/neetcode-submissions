class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        for num in nums: 
            counter = 0 
            curr = num 
            while curr in nums: 
                curr += 1 
                counter += 1 
            res = max(res, counter)

        return res