class Solution(object):
    def isSymmetric(self, root):
        def tree(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            return left.val == right.val and tree(left.left, right.right) and tree(left.right, right.left)

        return tree(root.left, root.right)