# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pass

def Value2Instance(ValueList):
    Node = ListNode(ValueList[0])
    Root = Node
    for i in range(1, len(ValueList)):
        Node.next = ListNode(ValueList[i])
        Node = Node.next
    return Root

if __name__ == "__main__":
    sys.stdout.write("Input list: \n")
    l1 = list(map(int, list(str(sys.stdin.readline()).strip())))
    sys.stdout.write("Result is: \n" + str(Solution().swapPairs(Value2Instance(l1))))