import sys
import time

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pass

if __name__ == "__main__":
    sys.stdout.write("Input list1: \n")
    l1 = list(map(int, [str(sys.stdin.readlines()).strip('->').strip('\n')]))
    print(l1)
    sys.stdout.write("Input list2: \n")    
    l2 = sys.stdin.readlines().strip("->")
    
    sys.stdout.write("Result is: \n" + str(Solution().mergeTwoLists(l1, l2)))