class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def countNodes(self, root):
        leftdepth = self.GetDepth(root, True)
        rightdepth = self.GetDepth(root, False)
        if leftdepth == rightdepth:
            return 2 ** leftdepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def GetDepth(self, root, isleft):
        if root == None:
            return 0
        elif isleft:
            return 1 + self.GetDepth(root.left, isleft)
        else:
            return 1 + self.GetDepth(root.right, isleft)

if __name__ == "__main__":
    Node1 = TreeNode(1)
    Node2 = TreeNode(2)
    Node3 = TreeNode(3)
    Node4 = TreeNode(4)
    Node5 = TreeNode(5)
    Node6 = TreeNode(6)
    Node7 = TreeNode(7)
    Node1.left = Node2
    Node1.right = Node3
    Node2.left = Node4
    Node2.right = Node5
    Node4.left = Node6
    Node4.right = Node7
    print(Solution().countNodes(Node1))