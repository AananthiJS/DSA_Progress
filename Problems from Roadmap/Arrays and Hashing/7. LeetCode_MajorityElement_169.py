class Solution:
    def majorityElement(self, nums) -> int:
        #Approach 1
        #counter = Counter(nums)
        #return max(counter, key = counter.get)

        #Approach 2 - Boyes-Moore approach (Useful when the majority element exist more than half the size of the list)
        majority = nums[0]
        count = 0
        for n in nums:
            if n == majority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority = n
                    count += 1

        return majority