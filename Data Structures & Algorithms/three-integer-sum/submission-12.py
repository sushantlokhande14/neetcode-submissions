class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for storing the final result 
        res = []
        nums.sort()

        for i, v in enumerate(nums): 

            if i >0 and v ==nums[i-1]: 
                continue 

            # declare the left and right pointers: 

            l = i + 1  #for we skipp the first position ___ + ___ + ___ = 0 
            r = len(nums)-1 

            #while loop 

            while l < r: 

                threeSum = v+ nums[l]+ nums[r]

                if threeSum < 0 : 
                    l+=1 
                
                elif threeSum > 0 : 
                    r-=1 

                else:  
                    res.append([v, nums[l],nums[r]])
                    l +=1 
                    r -=1 

                    while l < r and nums[l]==nums[l-1]: 
                        l+=1 

                    while l<r and nums[r]== nums[r+1]:
                        r-=1 

                
        return res 

                
