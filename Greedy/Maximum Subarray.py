'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

class Solution(object):
    # def maxSubArray(self, nums):
    #     arr = []
    #     arr.append(nums[0])
    #     m = arr[0]
    #     # Dynamic Programming:
    #     # arr[i] is the 'largest' sum of all subarray from the start till i
    #     # but we still keep track maximum 'm' cause largest until i doesn't mean largest subarray
    #     for i in range(1, len(nums)):
    #         arr.append( max( (arr[i-1] + nums[i]), nums[i] ) )
    #         if m < arr[i]:
    #             m = arr[i]
    #     return m
    
    def maxSubArray(self, nums):
        # Same concept Dynamic Programming
        # but only keep track maxSum and doesn't need extra memory for array
        currentSum = 0
        maxSum = -10**4
        for num in nums:
            currentSum += num
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0
        return maxSum