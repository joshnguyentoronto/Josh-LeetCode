'''
Given a binary tree, determine if it is height-balanced.

'''


class Solution(object):
    def isBalanced(self, node):
        val, hei = self.helper(node)
        if val:
            return True
        else:
            return False


    def helper(self, node):
        if not node:
            return True, 0
        elif not node.left and not node.right:
            return True, 1
        elif not node.left and node.right:
            valid, height = self.helper(node.right)
            if not valid:
                return False, 0
            elif height > 1:
                return False, 0
            else:
                return True, height + 1
        elif node.left and not node.right:
            valid, height = self.helper(node.left)
            if not valid:
                return False, 0
            elif height > 1:
                return False, 0
            else: 
                return True, height + 1
        elif node.left and node.right:
            left_val, left_height = self.helper(node.left)
            right_val, right_height = self.helper(node.right)
            if not left_val or not right_val:
                return False, 0
            elif abs(left_height - right_height) > 1:
                return False, 0
            elif left_height > right_height:
                return True, left_height + 1
            else:
                return True, right_height + 1