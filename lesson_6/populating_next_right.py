class Solution(object):
    def connect(self, root):
        def f2(node):
            if node.left:
                if node.right:
                    node.left.next = node.right
                    if node.next:
                        node.right.next = f2(node.next)
                else:
                    if node.next:
                        node.left.next = f2(node.next)

                return node.left
            else:
                if node.right:
                    if node.next:
                        node.right.next = f2(node.next)
                    return node.right
                else:
                    if node.next:
                        return f2(node.next)

        def f1(node):
            if node.left:
                if node.right:
                    node.left.next = node.right
                    if node.next:
                        node.right.next = f2(node.next)
                else:
                    if node.next:
                        node.left.next = f2(node.next)
            else:
                if node.right:
                    if node.next:
                        node.right.next = f2(node.next)

            if node.left:
                f1(node.left)

            if node.right:
                f1(node.right)

        if root:
            f1(root)

        return root