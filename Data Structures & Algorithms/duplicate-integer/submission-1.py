class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        primary_list=[]
        for number in nums:
            if number in primary_list:
                return True
            else: 
                primary_list.append(number)
            
        return False 