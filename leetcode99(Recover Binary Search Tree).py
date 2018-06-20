import sys

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        pass

if __name__ == "__main__":
    Node1 = TreeNode(1)
    Node2 = TreeNode(3)
    Node3 = TreeNode(None)
    Node4 = TreeNode(None)
    Node5 = TreeNode(2)
    Node1.left = Node2
    Node1.right = Node3
    Node2.left = Node4
    Node2.right = Node5
    Solution().recoverTree(Node1)
    sys.stdout.write(str(Node1.val) + str(Node2.val) + str(Node3.val) + str(Node4.val) + str(Node5.val))