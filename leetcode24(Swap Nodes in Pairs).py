import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swapHelper(anode):
            if anode.next:
                if anode.next.next:
                    temp = anode.next.next
                    anode.next.next = temp.next
                    temp.next = anode.next
                    anode.next = temp
                    swapHelper(temp.next)
                        
        if not head or not head.next:
            return head
        else:
            res = head.next
            head.next = head.next.next
            res.next = head
            swapHelper(head)
        #return res
        result = []
        while res:
            result.append(res.val)
            res = res.next

        return result

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