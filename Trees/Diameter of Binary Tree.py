'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
'''

# Find max depth of left and right side of each node to determine the max diameter
# Find max diameter of each node and compare it, choose the longest one
class Solution(object):
    def diameterOfBinaryTree(self, root):
        a = self.depth(root, 0)
        return max((a[0]+a[1]), a[2])

    def depth(self, node, diameter):
        if node is None:
            return [0, 0, diameter]
        elif not node.left and not node.right:
            return [0, 0, diameter]
        elif not node.left and node.right:
            a = self.depth(node.right, diameter)
            return [0, (max(a[0], a[1]) + 1), max(diameter, (a[0]+a[1]), a[2])]
        elif node.left and not node.right:
            a = self.depth(node.left, diameter)
            return [(max(a[0], a[1]) + 1), 0, max(diameter, (a[0]+a[1]), a[2])]
        else:
            a = self.depth(node.left, diameter)
            b = self.depth(node.right, diameter)
            return [
                (max(a[0], a[1]) + 1),
                (max(b[0], b[1]) + 1),
                (max(diameter, (a[0]+a[1]), (b[0]+b[1]), a[2], b[2]))
            ]
