def sorting(arr):
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1
        
    return arr
    
arr = [6, 5, 4, 3, 2, 1]
print(sorting(arr))


# I once thought why not use arr[i] instead of arr[j+1], in this case, you can't
# Because i stays in one place, i.e. the current element.
# j moves backwards till it find its place. so can't do arr[i] comparison.