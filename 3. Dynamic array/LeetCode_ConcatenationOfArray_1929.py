class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Find the length of nums
        nums_length = len(nums)

        #Double it and assign to ans
        ans_length = nums_length * 2
        ans = [0] * ans_length

        #Iterate through each i in nums, copy the element in ans[i] and ans[i+n]
        for i in range(nums_length):
            ans[i] = ans[i + nums_length] = nums[i]

        return ans 
    
sol = Solution()
print(sol.getConcatenation([1,2,1]))
# Time complexity: O(n)
# Space complexity: O(n)

