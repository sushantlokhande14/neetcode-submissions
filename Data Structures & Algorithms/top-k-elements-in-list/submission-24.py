class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map ={}
        for num in nums: 
            counter_map[num] = counter_map.get(num, 0) +1 
        arr = []
        for num, freq in counter_map.items(): 
            arr.append([freq, num])
        
        arr.sort(reverse = True)
        res = []
        for i in range(k): 
            res.append(arr[i][1])

        return res



