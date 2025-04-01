class Solution:
    def threeSum(self, nums) :
        answer = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    answer.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
        return answer
