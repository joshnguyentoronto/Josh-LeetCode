'''
Given a string s, find the length of the longest substring without repeating characters.



Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(s):
        if len(s) <= 1:
            return len(s)
        l, r = 0, 0
        a = 0
        char = set()
        char.add(s[0])
        while l <= r:
            if r == len(s) - 1:
                break
            elif (r < len(s) - 1) and (s[r+1] in char):
                char.discard(s[l])
                l += 1
                if l - r == 1:
                    r += 1
                    char.add(s[r])
                    a = max(a, r-l+1)
            else:
                r += 1
                char.add(s[r])
                a = max(a, r-l+1)
        return a



print(Solution.lengthOfLongestSubstring("abcabcbb"))