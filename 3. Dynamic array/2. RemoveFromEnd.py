#Class creation
class Array:
    #Constructor
    def __init__(self):
        self.capacity = 8
        self.length = 6
        self.arr = [2,3,4,5,6,7,0,0]
    
    #Approach 1: 
    # Popping the last element of the array
    # Time complexity: O(1)
    # Space complexity: O(1)
    # Reassignment to the same array is possible
    

    def popback(self):
        if self.length > 0:
            print("Popped the last element", self.arr[self.length-1],"from the array.")
            self.arr[self.length-1] = 0
            self.length -= 1
        else:
            print("Error! The array is empty")
            print(self.arr)

    #Approach 2:
    # Ignoring the last element of the array
    # The original array stays the same
    # Since the length is decremented, the last element is ignored
    # The spaces are still occupied by the popped elements
    # Since we are just decrementing the length, while pushing back some other element, 
    # the spaces are overwritten by the new element.

    def popback(self):
        if self.length > 0:
            self.length -= 1
        
MyArr = Array()
MyArr.popback()
MyArr.popback()
MyArr.popback()
MyArr.popback()
MyArr.popback()
MyArr.popback()
MyArr.popback()


#OUTPUT for Approach 1:

#Popped the last element 7 from the array.
#[2, 3, 4, 5, 6, 0, 0, 0]
#Popped the last element 6 from the array.
#[2, 3, 4, 5, 0, 0, 0, 0]
#Popped the last element 5 from the array.
#[2, 3, 4, 0, 0, 0, 0, 0]
#Popped the last element 4 from the array.
#[2, 3, 0, 0, 0, 0, 0, 0]
#Popped the last element 3 from the array.
#[2, 0, 0, 0, 0, 0, 0, 0]
#Popped the last element 2 from the array.
#[0, 0, 0, 0, 0, 0, 0, 0]
#Error! The array is empty
#[0, 0, 0, 0, 0, 0, 0, 0]
#
#=== Code Execution Successful ===