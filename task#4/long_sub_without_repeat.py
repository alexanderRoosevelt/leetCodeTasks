#Given a string s, find the length of the longest 
# substring
#  without repeating characters



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_indices = {}  # Dictionary to store characters and their last seen indices
        max_length = 0  # Maximum length of the substring
        start = 0  # Start index of the current substring

        for end in range(len(s)):
            if s[end] in char_indices and char_indices[s[end]] >= start:
            
                start = char_indices[s[end]] + 1

            char_indices[s[end]] = end

            max_length = max(max_length, end - start + 1)

        return max_length

        
        