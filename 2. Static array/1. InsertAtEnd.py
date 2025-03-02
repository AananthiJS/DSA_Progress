
#To practice the syntax, calculating the length of an array
def calcLength(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:
            return (i+1)

#Inserting the element at the end of the array
def InsertAtEnd(arr, n):
    length = calcLength(arr)
    capacity = len(arr)
    
    arr[length] = n
    
    print(arr)
    
InsertAtEnd([2,4,6,8,0,0], 10)

#OUTPUT

#[2,4,6,8,10,0]