'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''

class Solution:
    def generateParenthesis( n):
        res = []
        stack = [ [ '(', 1, 0 ] ]
        while stack:
            a = stack.pop()
            if a[1] < n:
                new = [  a[0]+'(',   a[1]+1,   a[2]  ]
                stack.append(new)
            if a[2] < n and a[2] < a[1]:
                new = [  a[0]+')',   a[1],   a[2]+1  ]
                stack.append(new)
            if a[1] == n and a[2] == n:
                res.append(a[0])
        return res

print(Solution.generateParenthesis(3))