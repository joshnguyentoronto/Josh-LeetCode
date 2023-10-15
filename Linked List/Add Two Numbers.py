'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# My Solution
# Run 45.3%, Space 95.92%
# Run 96.8%, Space 77.71%
class Solution:
    def addTwoNumbers(self, l1, l2):
        extra = 0
        head = None
        pivot = ListNode(0)
        while l1 or l2:
            if l1 and not l2:
                res = l1.val + extra
                extra = 0
                l1 = l1.next
                if res // 10 > 0:
                    extra = res // 10
                    res = res % 10
            elif l2 and not l1:
                res = l2.val + extra
                extra = 0
                l2 = l2.next
                if res // 10 > 0:
                    extra = res // 10
                    res = res % 10
            else:
                res = l1.val + l2.val + extra
                extra = 0
                l1, l2 = l1.next, l2.next
                if res // 10 > 0:
                    extra = res // 10
                    res = res % 10
            node = ListNode(res)
            pivot.next = node
            pivot = node
            if not head:
                head = node
        if extra != 0:
            node = ListNode(extra)
            pivot.next = node
        return head