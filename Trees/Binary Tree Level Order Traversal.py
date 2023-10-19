'''
Given the root of a binary tree, 
return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
'''

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            a = []
            l = len(queue)
            for i in range(l):
                node = queue.pop(0)
                a.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(a)
        return res