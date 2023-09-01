'''
Given the roots of two binary trees p and q, 
    write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.


Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''

class Solution:
    def isSameTree(self, p, q):
        return self.helper(p, q)

    # Compare 2 trees
    def helper(self, node1, node2):
        if not node1 and not node2:
            return True
        elif (not node1 or not node2) or (node1.val != node2.val):
            return False
        else:
            return self.helper(node1.left, node2.left) and self.helper(node1.right, node2.right)
