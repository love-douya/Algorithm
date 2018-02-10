def insert_sort(lists):
    #insert sort
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

list_test = [3,8,1,2,10,12]
result = insert_sort(list_test)
print(result)
