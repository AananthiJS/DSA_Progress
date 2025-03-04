class Solution:
    def twoSum(self, nums, target):
        total = 0
        hashmap = {}
        out = []

        for i in range(len(nums)):
            check = target - nums[i]
            if check in hashmap:
                out.append(hashmap[check])
                out.append(i)
            else:
                hashmap[nums[i]] = i                
        return out