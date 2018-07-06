import sys
import time
import copy

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not l1 : return l2
#         if not l2 : return l1
        
#         curr = head = ListNode(0)        
#         while l1 and l2:
#             if l1.val < l2.val:                
#                 curr.next = l1
#                 l1=l1.next                
#             else:                
#                 curr.next = l2
#                 l2=l2.next
#             curr = curr.next
        
#         curr.next = l1 if l1 else l2
            
#         return head.next

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        
        if not l2:
            return l1

        if l1.val <= l2.val:
            root = l1
            l1 = l1.next
        else:
            root = l2
            l2 = l2.next

        l3 = root

        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next
        
        #Runtime beats 97.38 %
        if l1:
            l3.next = l1
        else:
            l3.next = l2

        # # Also Runtime Beats 97.38 %
        # if l1:
        #     while l1:
        #         l3.next = l1
        #         l1 = l1.next
        #         l3 = l3.next

        # else:
        #     while l2:
        #         l3.next = l2
        #         l2 = l2.next
        #         l3 = l3.next

        result = []
        while root:
            result.append(root.val)
            root = root.next

        return result

def Value2Instance(ValueList):
    Node = ListNode(ValueList[0])
    Root = Node
    for i in range(1, len(ValueList)):
        Node.next = ListNode(ValueList[i])
        Node = Node.next

    # #Test
    # result = []
    # while Root:
    #     result.append(Root.val)
    #     Root = Root.next
    # print(result)

    return Root

if __name__ == "__main__":
    sys.stdout.write("Input list1: \n")
    l1 = list(map(int, list(str(sys.stdin.readline()).strip())))
    sys.stdout.write("Input list2: \n")    
    l2 = list(map(int, list(str(sys.stdin.readline()).strip())))
    #print("l1: {0}\nl2: {1}".format(l1, l2))
    sys.stdout.write("Result is: \n" + str(Solution().mergeTwoLists(Value2Instance(l1), Value2Instance(l2))))