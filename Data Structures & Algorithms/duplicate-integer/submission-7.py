class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp = set()

        for number in nums : 
            if number in mapp: 
                return True 
            else: 
                mapp.add(number)

        return False 

        