'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for char in s:
            if char in par.values():
                stack.append(char)
            elif char in par.keys():
                if stack == [] or par[char] != stack.pop():
                    return False
            else:
                return False
        return not stack