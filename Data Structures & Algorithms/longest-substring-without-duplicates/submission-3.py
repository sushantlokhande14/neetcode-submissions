class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset= set()
        res = 0 
        l = 0 

        for r in range(len(s)): 
            while s[r] in charset: 
                charset.remove(s[l]) # remove leftmost 
                l+=1 #update left 


            charset.add(s[r])
            res = max(res , len(charset))
        
        return res 
