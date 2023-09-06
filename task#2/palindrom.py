# Given an integer x, return true if x is a 
# palindrome, and false otherwise


class Solution(object):
    def isPalindrome(self, x):
        res = str(x)
        temp = ''.join(reversed(res))
        if(temp == res):
            return True
        else:
            return False
        
        