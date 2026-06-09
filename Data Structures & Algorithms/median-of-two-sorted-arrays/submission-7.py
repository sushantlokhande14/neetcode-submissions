class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0 
        j = 0 
        merged = []

        while i <= len(nums1)-1 and j <= len(nums2)-1:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i+=1 
            else: 
                merged.append(nums2[j])
                j+=1 
        # one of the arrays exhausted 
        while i<=len(nums1)-1:
            merged.append(nums1[i])
            i+=1 
            
        while j <= len(nums2)-1:
            merged.append(nums2[j])
            j+=1 
            

        mid = len(merged)//2 
        if len(merged)%2 == 0 : 
            res = (merged[mid-1]+ merged[mid])/2
        else: 
            res = merged[mid]
        
        return res 
