class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate(root):

    def traverse(node, prev):
        if node:
            print("node", node.val)
            if prev is not None and node.val > prev:
                print("found mismatch", node.val, prev)
                return False
            else:
                print("traversing down")
                return traverse(node.left, node.val) or traverse(node.right, node.val)
        else:
            print("no node")
            return False

    return traverse(root, None)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(validate(root))
