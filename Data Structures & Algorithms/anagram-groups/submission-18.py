class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = defaultdict(list)

        for word in strs: 
            charMap = [0] *26 
            for c in word: 
                charMap[ord(c)- ord('a')]+= 1 
            anagram_list[tuple(charMap)].append(word)

        return(list(anagram_list.values()))


