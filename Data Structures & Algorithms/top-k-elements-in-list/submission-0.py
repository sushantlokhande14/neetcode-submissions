class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = {}
        for num in nums:
            if str(num) not in counter_map:
                counter_map[str(num)] = 0 
            else: 
                current_count = counter_map[str(num)]
                counter_map[str(num)] = current_count +1 

        sorted_keys = sorted(counter_map, key=counter_map.get, reverse=True)  # Sort keys by values (descending)
        return sorted_keys[:k]  # Get the top K key