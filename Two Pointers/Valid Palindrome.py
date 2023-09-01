'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''


import re, math
class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'\W+', '', s)
        s = re.sub(r'[^A-Za-z0-9 ]', '', s)
        mid = int(math.floor(len(s) // 2))
        for i in range(0, mid):
            if s[i].lower() != s[len(s) - i - 1].lower():
                return False
        return True