'''
Design a class to find the kth largest element in a stream. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
    int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


Example 1:
    Input
    ["KthLargest", "add", "add", "add", "add", "add"]
    [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output
    [null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

'''

import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        # use heap cause it save time to add and delete number, second best option is binary search but it is O(n) insertion
        heapq.heapify(nums)
        # Make sure heap of size K cause we only need the Kth element, no more
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)
        # pop last element in heap (in array) to make sure heap of size K
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # last element in heap size K is the Kth element itself
        return self.nums[0]
