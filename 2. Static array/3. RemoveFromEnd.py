#To practice the syntax, calculating the length of an array
def calcLength(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:
            return (i+1)
        
#Removing the element at the end of the array
def RemoveFromEnd(arr):
    length = calcLength(arr)
    
    arr[length] = 0
    
    print(arr)
    
RemoveFromEnd([2,4,6,8,0,0])

#OUTPUT

#[2, 4, 6, 8, 0, 0]
#=== Code Execution Successful ===