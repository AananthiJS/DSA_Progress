class Array:
    def __init__ (self):
        self.capacity = 8
        self.length = 8
        self.arr = [2,4,6,8,10,12,20,30,40]
    
    def InsertInIndex(self, i, n):
        #Check if the array is full
        #If the array is full, resize the array
        if self.length >= self.capacity:
            self.arr = self.resize()
            print("Resized")

        #Check if the index is valid
        # If the index is valid, shift the elements to the right and insert the element at the index    
        if i <= self.length:
            for index in range(self.length, -1, -1):
                self.arr[index+1] = self.arr[index]
                if index == i:
                    self.arr[index] = n
                    self.length += 1
                    break
            
        print("Added the value", n, "at the index ", i)   
        print(self.arr)
    
    def resize(self):
        self.capacity = 2 * self.capacity
        self.newArr = [0] * self.capacity
        
        for i in range(self.length+1):
            self.newArr[i] = self.arr[i]

        return self.newArr
        
MyArr = Array()
MyArr.InsertInIndex(0, 20)
MyArr.InsertInIndex(3,40)

#OUTPUT:

#Added the value 20 at the index  0
#[20, 2, 4, 6, 8, 10, 12, 20, 30]
#Resized
#Added the value 40 at the index  3
#[20, 2, 4, 40, 6, 8, 10, 12, 20, 30, 0, 0, 0, 0, 0, 0]