class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list= []
        t_list= []
        for char_s in s: 
            s_list.append(char_s)
        for char_t in t: 
            t_list.append(char_t)
        s_list.sort()
        t_list.sort()
        if s_list == t_list: 
            return True 
        return False