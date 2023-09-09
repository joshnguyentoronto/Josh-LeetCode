'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
# Cause sorting the array will result in O(n Logn) so we cannot use it in our solution
# If we look at the sorted array: _, 1,2,3,4, _,100, _, 200, _
# Each sequence start with a number not exist in the array
# Which mean we can iterate throught the array and check if there is a number before the current number
# If we do, then we can skip it cause it's not the start of the array
# If we don't, then we can start a sequence and find the next number in the sequence while counting the length
# Note: Searching in array take lots of time, so we can convert it into a set (also help remove duplicate)
'''
Time: O(n) (loop through array once)
Space: O(n) (create a set)
'''
class Solution:
    def longestConsecutive(nums):
        numbers = set(nums)
        res = 0
        for num in numbers:
            if (num - 1) not in numbers:
                length = 0
                while (num + length) in numbers:
                    length += 1
                res = max(res, length)
        return res

print(Solution.longestConsecutive([100,4,200,1,3,2]))
print(Solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))