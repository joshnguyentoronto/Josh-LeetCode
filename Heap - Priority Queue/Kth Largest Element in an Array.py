'''
Given an integer array nums and an integer k, 
return the kth largest element in the array.

Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Can you solve it without sorting?


Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:
    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104
'''

# Solution with sort
# Pretty efficient: Run 87%, Space 89%
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]


# Solution with heap sort
# Run 21%, Space 95%
class Solution:
    def findKthLargest(self, nums, k):
        a = len(nums) - k
        heapq.heapify(nums)
        while a > 0:
            heapq.heappop(nums)
            a -= 1
        return heapq.heappop(nums)


# Solution without sort
# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1
        nums[fill], nums[right] = nums[right], nums[fill]
        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = self.partition(nums, left, right)
            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break
        return nums[k]