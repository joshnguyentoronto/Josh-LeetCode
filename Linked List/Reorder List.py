'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000
'''

# My solution:
class Solution:
    def reorderList(self, head):
        if head and head.next and head.next.next :
            # get middle of linked list
            count = 1
            mid = 1
            midNode = head
            temp1 = head
            while temp1:
                temp1 = temp1.next
                count += 1
                if count % 2 == 0:
                    a = count // 2
                    if a > mid:
                        mid = a
                        midNode = midNode.next
                else:
                    a = (count // 2) + 1
                    if a > mid:
                        mid = a
                        midNode = midNode.next
            # add each node after midNode to stack and set midNode.next = None
            stack = []
            temp2 = midNode.next
            while temp2:
                stack.append(temp2)
                temp2 = temp2.next
            midNode.next = None
            # pop from stack and insert into first half of the linked list
            while stack:
                temp3 = head.next
                head.next = stack.pop()
                head = head.next
                head.next = temp3
                head = head.next


