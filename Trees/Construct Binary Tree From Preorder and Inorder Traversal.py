'''
Given two integer arrays preorder and inorder 
where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree,

Construct and return the binary tree.


Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''


# My Solution
# Run 43%, Space 48%
class Solution:
    def buildTree(self, preorder, inorder):
        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        i = inorder[:mid]
        if i:
            node.left = self.buildTree(preorder[1:len(i)+1], i)
        f = inorder[mid+1:]
        if f:
            node.right = self.buildTree(preorder[len(i)+1:], f)
        return node

# Neetcode solution (more clean):
# Run 60%, Space 48%
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return node