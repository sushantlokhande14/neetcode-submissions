class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums: 
            if i in count: 
                count[i]= count[i]+1 
            else: 
                count[i] = 1 

        arr = []

        for num, c in count.items(): 
            arr.append([c , num])

        arr.sort()

        res = []

        for i in range(k):
            res.append(arr.pop()[1])

        return res 
            

        


