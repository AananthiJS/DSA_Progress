
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
def insertInMiddle(arr, i, n):
    length = calcLength(arr)
    if i <= length:
        #Traversing the array from right to left
        for index in range(len(arr) - 1, -1, -1):
            if index != i:
                arr[index] = arr[index - 1]
            else:
                arr[i] = n
                break
                
        printArr(arr)
    else:
        print("ERROR: i is out of range")
    
insertInMiddle([0,0,3,3,0], 3, 20)

#OUTPUT:

#Element in index  0  is:  0
#Element in index  1  is:  0
#Element in index  2  is:  3
#Element in index  3  is:  20
#Element in index  4  is:  3
#
#=== Code Execution Successful ===