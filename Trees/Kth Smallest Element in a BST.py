'''
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) 
of all the values of the nodes in the tree.


Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

# My solution:
# Run 6.37%, Space 99.95%
class Solution:
    def kthSmallest(self, root, k):
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node.right and not node.left:
                res.append(node.val)
            if node.right and not node.left:
                stack.append(node.right)
                node.right = None
                stack.append(node)
            elif node.right:
                stack.append(node.right)
                node.right = None
            if node.left:
                stack.append(node)
                stack.append(node.left)
                node.left = None
        return res[k-1]


# Needcode Solution
# Run 91%. Space 70%
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right