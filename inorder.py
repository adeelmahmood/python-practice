class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):

    def traverse(node):
        if node:
            traverse(node.left)
            print(node.val)
            traverse(node.right)

    traverse(root)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

inorder(root)
