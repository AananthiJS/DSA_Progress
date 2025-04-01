class Solution:
    def maxArea(self, height):
        # Brute force
        #res = 0
#
        #for i in range(len(height)):
        #    for j in range(i + 1, len(height)):
        #        res = max(res, min(height[i], height[j]) * (j - i))
#
        #return res

        # Two Pointers
        L, R = 0, len(height) - 1
        res = 0

        while L < R:
            area = (R - L) * min(height[L], height[R])
            res = max(res, area)

            if height[L] <= height[R]:
                L += 1
            elif height[R] <= height[L]:
                R -= 1

        return res