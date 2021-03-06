def quicksort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)

def quick_sort_helper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quick_sort_helper(alist, first, splitpoint - 1)
        quick_sort_helper(alist, splitpoint + 1, last)
        
def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
                
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1  

        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark - 1          
        
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

alist = [12, 1, 2, 3, 4, 5, 6, 7, 11]
quicksort(alist)
print(alist)



