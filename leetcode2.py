class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        visited  = []
        deep = 1
        flag = root
        while flag.left != None and flag.right and None:
            return
            
if __name__ == "__main__":
    Node1  = TreeNode(1)
    Node2 = TreeNode(2)
    Node3 = TreeNode(3)
    Node1.left = Node2
    node1.right = Node3

    


