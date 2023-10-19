'''
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.


Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''


class Solution:
    def rightSideView(self, root):
        res = []
        queue = []
        queue.append(root)
        while queue:
            l = len(queue)
            a = 0
            for i in range(l):
                node = queue.pop(0)
                if node and a == 0:
                    res.append(node.val)
                    a = 1234
                if node and node.right:
                    queue.append(node.right)
                if node and node.left:
                    queue.append(node.left)
        return res


