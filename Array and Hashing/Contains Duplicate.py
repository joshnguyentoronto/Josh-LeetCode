'''
Given an integer array nums, 
    return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

'''


class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) > len(set(nums)):
            return True
        else:
            return False


class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False

