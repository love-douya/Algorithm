#A silly solution
import copy
import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        iter_l1 = copy.deepcopy(l1)
        iter_l2 = copy.deepcopy(l2)
        num_current = (l1.val + l2.val) % 10
        num_previous = (l1.val + l2.val) // 10
        iter_l3 = ListNode(num_current)
        #initalize
        l3 = ListNode(0)
        l3.next = iter_l3
        iter_l1 = iter_l1.next
        iter_l2 = iter_l2.next
        while iter_l1 != None and iter_l2 != None:
            num_previous, num_current = divmod(iter_l1.val + iter_l2.val + num_previous, 10)
            #num_current = (iter_l1.val + iter_l2.val + num_previous) % 10
            #print(num_current)
            #num_previous = (iter_l1.val + iter_l2.val + num_previous) // 10
            iter_l3.next = ListNode(num_current)
            iter_l1 = iter_l1.next
            iter_l2 = iter_l2.next
            iter_l3 = iter_l3.next

        if iter_l1 == None and iter_l2 != None:
            while iter_l2 != None:
                num_current = (iter_l2.val + num_previous) % 10
                num_previous = (iter_l2.val + num_previous) // 10
                iter_l3.next = ListNode(num_current)
                iter_l3 = iter_l3.next
                iter_l2 = iter_l2.next
        
        elif iter_l2 == None and iter_l1 != None:
            while iter_l1 != None:
                num_current = (iter_l1.val + num_previous) % 10
                num_previous = (iter_l1.val + num_previous) // 10
                iter_l3.next = ListNode(num_current)
                iter_l3 = iter_l3.next
                iter_l1 = iter_l1.next

        else:
            pass

        if iter_l1 == None and iter_l2 == None and num_previous != 0:
            num_current = num_previous % 10
            iter_l3.next = ListNode(num_current)

        return l3.next     

if __name__ == "__main__":
    # Node1 = ListNode(2)
    # Node2 = ListNode(4)
    # Node3 = ListNode(3)
    # Node4 = ListNode(5)
    # Node5 = ListNode(6)
    # Node6 = ListNode(4)
    # Node1.next = Node2
    # Node2.next = Node3
    # Node4.next = Node5
    # Node5.next = Node6
    Node1 = ListNode(1)
    Node2 = ListNode(9)
    Node3 = ListNode(9)
    Node2.next = Node3
    l1 = copy.deepcopy(Node1)
    l2 = copy.deepcopy(Node2)
    l3 = Solution().addTwoNumbers(l1, l2)
    while l3 != None:
        sys.stdout.write(str(l3.val))
        l3 = l3.next
    