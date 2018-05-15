class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        pass

if __name__ == "__main__":
    Node1 = ListNode(2)
    Node2 = ListNode(4)
    Node3 = ListNode(3)
    Node4 = ListNode(5)
    Node5 = ListNode(6)
    Node6 = ListNode(4)
    Node1.next = Node2
    Node2.next = Node3
    Node4.next = Node5
    Node5.next = Node6
    l1 = Node1
    l2 = Node4
    print(Solution().addTwoNumbers(l1, l2))
    