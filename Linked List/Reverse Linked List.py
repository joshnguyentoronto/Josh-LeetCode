'''
Given the head of a singly linked list, reverse the list, and return the reversed list (head).

'''

class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            return self.helper(None, head, head.next)

    def helper(self, pre, node, next):
        if next is None:
            node.next = pre
            return node
        else:
            node.next = pre
            return self.helper(node, next, next.next)