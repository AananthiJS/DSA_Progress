class Solution:
    def productExceptSelf(self, nums):
        res = []
        pre = 1
        post = 1
        res.append(pre)
        n = len(nums)

        #Loop to create prefic list as output list
        for i in range(1, n):
            pre *= nums[i - 1]
            res.append(pre)

        #Loop through output to get postfix product and directly product it with nums
        for j in range(n-2, -1, -1):
            post *= nums[j + 1]
            res[j] = res[j] * post
        return res