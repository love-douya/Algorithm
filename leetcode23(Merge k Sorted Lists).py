import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2

        #return lists[0] if amount > 0 else lists

        result = []
        while lists[0]:
            result.append(lists[0].val)
            lists[0] = lists[0].next

        return result


    def mergeTwoLists(self, l1, l2):
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
        if l1:
            l3.next = l1
        else:
            l3.next = l2
        return root

def Value2Instance(ValueList):
    Node = ListNode(ValueList[0])
    Root = Node
    for i in range(1, len(ValueList)):
        Node.next = ListNode(ValueList[i])
        Node = Node.next
    return Root

if __name__ == '__main__':
    Num_lists = int(input('Input list number: '))
    lists = []
    for i in range(Num_lists):
        lists.append(Value2Instance(list(input('Input list: '))))
    print(Solution().mergeKLists(lists))