from collections import deque

A = [-12, 1, -17, 3, 4, 20]
Sort_A = []

def Max_Heapify(A, i):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= len(A) - 1 and A[l] > A[i]:
        largest = l
    else:
         largest = i
    if r <= len(A) - 1 and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, largest)

def Bulid_Max_Heap(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        Max_Heapify(A, i)

def Heapsort(A):
    Bulid_Max_Heap(A)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        temp = A.pop()
        Sort_A.append(temp)
        Max_Heapify(A, 0)

Heapsort(A)
print(Sort_A)
    