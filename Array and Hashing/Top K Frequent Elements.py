'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

class Solution:
    def topKFrequent(self, nums, k):
        if not nums:
            return nums
        diction = {}
        for num in nums:
            if num not in diction:
                diction[num] = 1
            elif num in diction:
                diction[num] += 1
        sortedDict = sorted(diction.items(), key=lambda item:item[1], reverse=True)
        arr = []
        for i in range(0, k):
            arr.append(sortedDict[i][0])
        return arr
