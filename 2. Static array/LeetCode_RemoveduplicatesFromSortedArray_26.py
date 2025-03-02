#Approach 1: Got TLE for this approach

#If duplicate is found in the array, replace it with 101 (101, because the question says that nums elements must be between -100 and 100)
#If the element is not a duplicate, increment j

def removeDuplicates(nums):
    n = len(nums)
    k = 0
    
    for j in range(n+1):
        for i in range(j+1, n):
            if j < n-1 and nums[j] == nums[i]:
                nums[i] = 101
                i = i + 1
            else:
                j = j + 1
    nums.sort()
    d = nums.count(101)
    k = n - d
    print(k)
    print(nums)
    
removeDuplicates([0,0,1,1,1,2,2,3,3,4])
removeDuplicates([1])

#OUTPUT:
#5
#[0, 1, 2, 3, 4, 101, 101, 101, 101, 101]
#1
#[1]

#Approach 2: Accepted Solution (Two pointers)

#k is the index of unique element.
#If another unique element is found, increment k and replace the element at index k with the element at index i
#Do nothing and just traverse through the array if the element is a duplicate

def removeDuplicates(nums):
    if not nums:
        return 0
    
    k = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
    
    k += 1
    
    print(k)
    print(nums[:k])
    
removeDuplicates([0,0,1,1,1,2,2,3,3,4])
removeDuplicates([1])

#OUTPUT:

#5
#[0, 1, 2, 3, 4]
#1
#[1]
#
#=== Code Execution Successful ===