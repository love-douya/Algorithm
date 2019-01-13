import sys

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        count = 1
        while count < n - 1:
            node = node.next
            count += 1
        node.next = node.next.next
        return head

    def Create_Node_List(self, sequence, length):
        start = ListNode(sequence[0])
        Node = start
        for i in range(1, length):
            Next_Node = ListNode(sequence[i])
            Node.next = Next_Node
            Next_Node = Node
        return start

    def Print_Node(self, start):
        while start:
            print(start.val)
            start = start.next

if __name__ == "__main__":
    sys.stdout.write("Input the link number sequence: \n")
    sequence = list(map(int, str(sys.stdin.readline()).strip().split()))
    length = len(sequence)
    sys.stdout.write("Input the number of the node to be deleted: \n")
    reverse_node_number = int(sys.stdin.readline())
    solution = Solution()
    solution.Print_Node(solution.removeNthFromEnd(solution.Create_Node_List(sequence, length), length))
    
    
    

    