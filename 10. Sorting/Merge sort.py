def MergeSort (arr, start, end):
    if end - start + 1 <= 1:
        return
   
    mid = (start + end) // 2
   
    MergeSort(arr, start, mid)
    MergeSort(arr, mid + 1, end)
    Merge(arr, start, mid, end)
   
    return arr
   
def Merge(arr, start, mid, end):
    L = arr[start : mid + 1]
    R = arr[mid + 1 : end + 1]
   
    i = 0
    j = 0
    k = start
   
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
   
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
   
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

arr = [6,7,4,3,2,1,8]
print(MergeSort(arr, 0, 6))