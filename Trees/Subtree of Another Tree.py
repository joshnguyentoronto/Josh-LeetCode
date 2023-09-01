'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
'''

class Solution:
    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root and subRoot: return False
        # BFS for each node in 'root' to compare to 'subRoot'
        if self.helper(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    # Check 2 tree the same (same tree problem)
    def helper(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val == node2.val:
            return ( self.helper(node1.left, node2.left) and self.helper(node1.right, node2.right) )
        return False
