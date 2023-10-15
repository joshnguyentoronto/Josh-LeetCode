'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

Follow up: Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# My solution: O(n)
#  Run 88%, Space 52%
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head.next:
            return None
        else: 
            temp = head
            temp1 = None
            temp2 = head
            count = 1
            while count <= n:
                if count == n:
                    while temp:
                        if not temp.next and not temp1 :
                            return temp2.next
                        elif not temp.next:
                            temp1.next = temp2.next
                            temp2 = None
                            return head
                        else:
                            temp1 = temp2
                            temp2 = temp2.next
                            temp = temp.next
                temp = temp.next
                count += 1