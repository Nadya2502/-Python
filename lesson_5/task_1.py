class Solution(object):
    def postorderTraversal(self, root):
        ans = []

        def helper(node):

            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            ans.append(node.val)

        if not root:
            return ans
        helper(root)
        return ans