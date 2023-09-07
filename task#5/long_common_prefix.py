# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longest_common_prefix(self, strs):
        if not strs:
            return ""

    # Find the shortest string in the array
        shortest = min(strs, key=len)

    # Initialize the prefix as the shortest string
        prefix = shortest

    # Iterate through the array of strings and compare characters
        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from the prefix

        return prefix

            
        

sol = Solution()
print(sol.longest_common_prefix(["flower","flow","flight"]))