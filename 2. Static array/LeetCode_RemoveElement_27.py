#Approach 1:  Accepted solution (Two pointers)

#k is the index of the element that is not equal to val
#If the element is not equal to val, replace the element at index k with the element at index i and increment k
#Do nothing and just traverse through the array if the element is equal to val

def removeElement(nums, val):
    k = 0
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1  
        
    print(nums)
    print(k)
    
removeElement([3,2,2,3], 3)
removeElement([0,1,2,2,3,0,4,2], 2)
removeElement([2,2,3], 2)

#OUTPUT:

#[2, 2, 2, 3]
#2
#[0, 1, 3, 0, 4, 0, 4, 2]
#5
#[3, 2, 3]
#1
#
#=== Code Execution Successful ===