# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import sys

print("test")

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pass

class Single_Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
if __name__ == "__main__":
    sys.stdout.write("Input the link number sequence: \n")
    sequence = list(map(int, str(sys.stdin.readline(input())).strip().split()))
    length = len(sequence)
    print("%s, %d" %sequence %length)
    
    

    