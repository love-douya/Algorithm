import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Others_Solution:
    # Using recursive to solve this problem;
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head

        tmp = cur = head
        idx = -1
        for i in range(k-1):
            if not cur or not cur.next: break
            idx = i
            cur = cur.next
        if idx != k - 2:
            return head
        nextHead = cur.next
        cur.next = None
        tail = self.reverse(tmp)
        head.next = self.reverseKGroup(nextHead, k)
        return tail
    
    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tempNext = cur.next
            cur.next, pre, cur = pre, cur, tempNext
        return pre

class MySolution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def swapHelper(anode):
            if anode.next and anode.next.next:
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
    l1 = list(map(str, list(str(sys.stdin.readline()).strip())))
    sys.stdout.flush()
    sys.stdout.write("Input 'K': \n")
    k = int(sys.stdin.read())
    sys.stdout.write("Address of the list head is: \n" + str(Others_Solution().reverseKGroup(Value2Instance(l1), k)))