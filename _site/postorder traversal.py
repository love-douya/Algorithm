class TreeNode(object):
    val = 0
    right = None
    left = None
    #constructor
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def postOrderUsingStack(node = None):
    visits = []
    stack = []
    if node is None:
        return
    stack.append(node)
    cur = node
    visited = None

    while len(stack) > 0:
        if cur is not None and cur.left is not None:
            stack.append(cur.left)
            cur = cur.left
        else:
            cur = stack[-1]
            #right child is not None and cur.right!=visited:
            if cur.right is not None and cur.right != visited:
                cur = cur.right
                stack.append(cur)
            else:
                #do a visit
                visits.append(cur.val)
                stack.pop()
                visited = cur
                cur = None
    return visits

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
vals = postOrderUsingStack(root)
print(vals)
