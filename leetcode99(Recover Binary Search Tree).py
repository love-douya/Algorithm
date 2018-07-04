import sys

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pre_node, self.n1, self.n2 = None, None, None
        self.solve(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        
    def solve(self, root):
        if not root:
            return self.solve(root.left)
        if not self.pre_node:
            self.pre_node = root
        if root.val < self.pre_node.val:
            if not self.n1:
                self.n1 = self.pre_node
                self.n2 = root
            else:
                self.n2 = root
        self.pre_node = root
        self.solve(root.right)

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        pass

if __name__ == "__main__":
    Node1 = TreeNode(1)
    Node2 = TreeNode(3)
    Node3 = TreeNode(0)
    Node4 = TreeNode(0)
    Node5 = TreeNode(2)
    Node1.left = Node2
    Node1.right = Node3
    Node2.left = Node4
    Node2.right = Node5
    Solution().recoverTree(Node1)
    sys.stdout.write(str(Node1.val) + str(Node2.val) + str(Node3.val) + str(Node4.val) + str(Node5.val))