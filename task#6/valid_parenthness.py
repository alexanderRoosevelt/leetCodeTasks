# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution(object):
    def isValid(self, s):
        stack = []  # Initialize an empty stack to store opening brackets

    # Define a mapping of opening and closing brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the input string
        for char in s:
        # If the character is a closing bracket
            if char in bracket_map:
            # Pop the top element from the stack if it exists; otherwise, use a dummy value '#'
                top_element = stack.pop() if stack else '#'
            
            # If the top element on the stack doesn't match the corresponding opening bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
            # If the character is an opening bracket, push it onto the stack
                stack.append(char)

    # After iterating through the entire string, the stack should be empty if it's a valid expression
        return not stack