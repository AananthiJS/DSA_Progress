from collections import deque

class Postfix():
    def __init__(self):
        self.arr = [2, 3, 7, 1, 5]
        self.length = len(self.arr)

        totalSum = 0
        totalProduct = 1
        self.postfixSum = deque()
        self.postfixProduct = deque()

        self.postfixSum.appendleft(0)
        self.postfixProduct.appendleft(1)

        for i in range(len(self.arr) - 1, -1, -1):
            totalSum += self.arr[i]
            self.postfixSum.appendleft(totalSum)

            totalProduct *= self.arr[i]
            self.postfixProduct.appendleft(totalProduct)
        
        self.postfixSum = list(self.postfixSum)
        self.postfixProduct = list(self.postfixProduct)

    def subArray_sum(self, Left, Right):
        subArray = 0
        if Left > Right:
            return ("Inalid Left and Right indices")
        elif Right > self.length:
            return ("Right index out of bounds")
        elif Right == self.length - 1:
            self.postfixSum[Right + 1] = 0
        subArray = self.postfixSum[Left] - self.postfixSum[Right +  1]
        return subArray
    
    def subArray_product(self, Left, Right):
        subArray = 0
        if Left > Right:
            return ("Invalid Left and Right indices")
        elif Right > self.length:
            return ("Right index out of bounds")
        elif Right == self.length - 1:
            self.postfixProduct[Right + 1] = 1
        subArray = self.postfixProduct[Left] / self.postfixProduct[Right + 1]
        return subArray
    
obj = Postfix()
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