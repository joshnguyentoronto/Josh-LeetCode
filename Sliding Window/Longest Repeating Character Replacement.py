'''
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.


Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: 
    Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
    There may exists other ways to achive this answer too.
'''

# My solution
class Solution:
    def characterReplacement(self, s, k):
        res, l, r = 0, 0 ,0
        map = {}
        if k == 0:
            res = 1
            l, r = 0, 1
            for i in range(2):
                if s[i] in map.keys():
                    map[s[i]] += 1
                else:
                    map[s[i]] = 1
        elif k != 0:
            res = 2
            l, r = 0, 2
            for i in range(3):
                if s[i] in map.keys():
                    map[s[i]] += 1
                else:
                    map[s[i]] = 1

        while l <= len(s)-1:
            if len(map) == 1 :
                res = max(res, list(map.values())[0])
                if r == len(s)-1:
                    break
                else:
                    r += 1
                    if s[r] in map.keys():
                        map[s[r]] += 1
                    else:
                        map[s[r]] = 1
            else:
                window = r-l+1
                a = max(list(map.values()))
                b = window - a
                if b <= k:
                    res = max(res, window)
                    if r == len(s)-1:
                        break
                    else:
                        r += 1
                        if s[r] in map.keys():
                            map[s[r]] += 1
                        else:
                            map[s[r]] = 1
                else: 
                    map[s[l]] -= 1
                    l += 1
        return res


# Leetcode solution:
class Solution:
    def characterReplacement(self, s, k):
        map = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            map[s[r]] = 1 + map.get(s[r], 0)
            maxf = max(maxf, map[s[r]])
            while (r-l+1) - maxf > k:
                map[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        return res