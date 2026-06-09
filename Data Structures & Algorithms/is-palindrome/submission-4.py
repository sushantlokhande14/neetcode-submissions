class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for i in s: 
            if i.isalnum():
                string.append(i.lower())
        reverse = string[::-1]
        if string == reverse: 
            return True 
        else :
            return False 

                  