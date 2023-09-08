'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# O(n) solution:
'''
Using prefix and postfix of the array
            origin:  [  1,  2,  3, 4  ]

prefix is multiply from a - z, keep the 1st element the same
            prefix:  [  1,  2,  6, 24 ]
    shifted-prefix:  [  1,  1,  2,  6 ]  24

postfix is multiply from z - a, keep the last element the same
            postfix: [ 24, 24, 12,  4 ]
shifted-postfix:  24 [ 24, 12,  4,  1 ]

output is multiply of shifted-prefix and shifted-postfix
output:  [ 24, 12,  8, 6  ]

** we can even save space by calculate prefix and put it in result array,
    then calculate postfix and multiply with existing prefix in the result array
    (using pre and post integer to calculate prefix and postfix)

time: O(2n) -> O(n)
'''

class Solution:
    def productExceptSelf(self, nums):


# O(1) solution challenge:
'''
class Solution:
    def productExceptSelf(self, nums):

'''