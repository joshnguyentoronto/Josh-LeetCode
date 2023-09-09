'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''


# a little brute force plus 2sum method
# Time limit exceed
class Solution:
    def threeSum(self, nums):
        res = []
        for i in range(len(nums)):
            temp = nums
            temp[i], temp[0] = temp[0], nums[i]
            newTarget = 0 - temp[0]
            d = {}
            for j in range(1, len(temp)):
                if newTarget - temp[j] in d:
                    a = [ d[newTarget - temp[j]], temp[j], temp[0] ]
                    a.sort()
                    if a not in res:
                        res.append(a)
                else:
                    d[temp[j]] = temp[j]
        return res


# Sort the array O(n logn)
# iterate through each number, check that number with another two number that have pointer l, r
# Time: O(n^2)
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue
            l, r = idx + 1, len(nums) - 1
            while l < r:
                n = num + nums[l] + nums[r]
                if n > 0:
                    r -= 1
                elif n < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    # skip duplicate and search for another result with the same int:sum
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res