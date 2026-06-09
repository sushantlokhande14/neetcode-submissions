class Solution(object):
    def groupAnagrams(self, strs):
        mapp = {}  # Regular dictionary
        for word in strs:
            sorted_word = ''.join(sorted(word))  # Sort to form the key
            if sorted_word not in mapp:
                mapp[sorted_word] = []  # Initialize list if key is missing
            mapp[sorted_word].append(word)  # Append word to the list
        return list(mapp.values())  # Convert to list of lists