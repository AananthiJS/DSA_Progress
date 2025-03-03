class Prefix:
    def __init__(self):
        self.arr = [2, 3, 7, 1, 5]
        self.length = len(self.arr)
        self.prefix_sum = []
        self.prefix_product = []

        #Prefix sum and product of all elements        
        total_sum = 0
        total_product = 1
        for i in range(self.length):
            total_sum += self.arr[i]
            self.prefix_sum.append(total_sum)

            total_product *= self.arr[i]
            self.prefix_product.append(total_product)

    def subArray_sum(self, Left, Right):
        subArray = 0
        if Left > Right:
            return ("Invalid Left and Right indices")
        elif Right > self.length:
            return ("Right index out of bounds")
        elif Left == 0:
            self.prefix_sum[Left - 1] = 0
        subArray = self.prefix_sum[Right] - self.prefix_sum[Left - 1]
        return subArray
    
    def subArray_product(self, Left, Right):
        subArray = 0
        if Left > Right:
            return("Invalid Left and Right indices")
        elif Right > self.length:
            return ("Right index out of bounds")
        elif Left == 0:
            self.prefix_product[Left - 1] = 1
        subArray = self.prefix_product[Right] / self.prefix_product[Left - 1]
        return subArray
    
obj = Prefix()
print(obj.subArray_sum(1,3))
print(obj.subArray_sum(3,4))
print(obj.subArray_sum(3,3))
print(obj.subArray_sum(0,3))
print(obj.subArray_sum(1,9))
print(obj.subArray_sum(4,3))

print(obj.subArray_product(1,3))
print(obj.subArray_product(3,4))
print(obj.subArray_product(2,2))
print(obj.subArray_product(0,3))
print(obj.subArray_product(1,9))
print(obj.subArray_product(4,3))