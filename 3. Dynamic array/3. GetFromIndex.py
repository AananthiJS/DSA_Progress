#Class creation
class Array:
    #Constructor
    def __init__(self):
        self.length = 4
        self.capacity = 4
        self.arr = [2,3,4,5]

    #Gets the element from the index i. If the index does not exist, it prints that the index does not exist    
    def GetFromIndex(self,i):
        if i < self.length:
            print("The element in index ", i, " is ", self.arr[i] )
        else:
            print("The index ", i, " does not exist")
            
MyArr = Array()
MyArr.GetFromIndex(3)
MyArr.GetFromIndex(1)
MyArr.GetFromIndex(5)
MyArr.GetFromIndex(4)

#OUTPUT:

#The element in index  3  is  5
#The element in index  1  is  3
#The index  5  does not exist
#The index  4  does not exist