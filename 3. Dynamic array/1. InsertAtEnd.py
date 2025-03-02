#defining a class for the dynamic array
class Array:
    #constructor to initialize the attributes to an object
    def __init__(self): #Self is a reference to keep track of current object
        self.capacity = 2
        self.length = 0
        self.array = [0] * self.capacity

    #Pushing an element at the end of the array
    def pushback(self, n):
        if self.length < self.capacity:
            self.arr[self.length] = n #assigning n to the last element of the array
            self.length += 1
            print("Array after inserting ", n, ": ",self.arr)
        else:
            print("Ran out of space. Resizing")
            self.arr = self.resize()
            self.arr[self.length] = n
            self.length += 1
            print("Array after inserting ", n, ": ", self.arr)

    #Resizing the array
    def resize(self):
        #Doubling the capacity of the array
        self.capacity = 2 * self.capacity
        self.newArr = [0] * self.capacity
        
        #Copying the elements of the old array to the new array
        for i in range(len(self.arr)):
            self.newArr[i] = self.arr[i]
            
        print("Capacity of newArr: ", self.capacity)
            
        return self.newArr
        
MyArr = Array() #Object creation
MyArr.pushback(2) #function call
MyArr.pushback(3)
MyArr.pushback(4)
MyArr.pushback(5)
MyArr.pushback(6)
MyArr.pushback('P')
MyArr.pushback('S')
MyArr.pushback('G')
MyArr.pushback('A')

# Time complexity: O(n)
# Space complexity: O(n)

#OUTPUT:

#Array after inserting  2 :  [2, 0]
#Array after inserting  3 :  [2, 3]
#Ran out of space. Resizing
#Capacity of newArr:  4
#Array after inserting  4 :  [2, 3, 4, 0]
#Array after inserting  5 :  [2, 3, 4, 5]
#Ran out of space. Resizing
#Capacity of newArr:  8
#Array after inserting  6 :  [2, 3, 4, 5, 6, 0, 0, 0]
#Array after inserting  P :  [2, 3, 4, 5, 6, 'P', 0, 0]
#Array after inserting  S :  [2, 3, 4, 5, 6, 'P', 'S', 0]
#Array after inserting  G :  [2, 3, 4, 5, 6, 'P', 'S', 'G']
#Ran out of space. Resizing
#Capacity of newArr:  16
#Array after inserting  A :  [2, 3, 4, 5, 6, 'P', 'S', 'G', 'A', 0, 0, 0, 0, 0, 0, 0]
#
#=== Code Execution Successful ===