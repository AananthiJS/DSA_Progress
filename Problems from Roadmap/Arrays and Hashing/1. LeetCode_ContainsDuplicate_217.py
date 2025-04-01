class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashMap = {}

        if len(nums) == 1:
            return False
        else:
            for i in nums:
                if i not in hashMap:
                    hashMap[i] = 1
                else:
                    return True
        return False
    
        #APPROACH 2
        hashset = set()

        for i in nums:
            if i not in hashset:
                hashset.add(i)
            else:
                return True
        return False
    
obj = Solution()
obj.containsDuplicate([1,2,3,1])


#Optimised solution:
#return len(set(nums)) != len(nums)