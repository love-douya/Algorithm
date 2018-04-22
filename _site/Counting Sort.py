def Counting_Sort(A, B, k):
    C = [None] * k
    for i in range(0, k):
        C[i] = 0
    for j in range(0, len(A)):
        C[A[j]] += 1 # C[i] now contains the number of elements equal to i.
    for i in range(1, k):
        C[i] = C[i] + C[i - 1] # C[i] now contains the number of elements less than or equal to i.
    for j in range(0, len(A)):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

A = [2, 5, 3, 0, 2, 3, 0, 3]
B = [None] * len(A)
Counting_Sort(A, B, 6)
print(B)
