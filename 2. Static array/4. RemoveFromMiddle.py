
#To practice the syntax, finding the length of an array
def calcLength(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:
            return i + 1
    return 0

#To practice the syntax, printing the elements of an array
def printArr(arr):
    for i in range(len(arr)):
        print("Element in index ", i, " is: ", arr[i])
 
#Removing the element at index i and shifting the elements to the left 
def removeFromMiddle(arr, i):
    length = calcLength(arr)
    
    arr[i] = arr[i+1]
    
    for index in range(i+1, length-1):
        arr[index] = arr[index + 1]
        
    arr[length - 1] = 0
    
    printArr(arr)
    
removeFromMiddle([2,4,6,8,10,9,8], 3)

#OUTPUT:

#Element in index  0  is:  2
#Element in index  1  is:  4
#Element in index  2  is:  6
#Element in index  3  is:  10
#Element in index  4  is:  9
#Element in index  5  is:  8
#Element in index  6  is:  0