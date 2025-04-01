class Solution:
    def trap(self, height):
        maxLeft = height[0]
        maxRight = height[-1]
        area = 0
        L, R = 0, len(height) - 1

        while L < R:
            if maxLeft <= maxRight:
                L += 1
                if min(maxLeft, maxRight) - height[L] > 0:
                    area += min(maxLeft, maxRight) - height[L]
                maxLeft = max(height[L], maxLeft)

            elif maxRight < maxLeft:
                R -= 1
                if min(maxLeft, maxRight) - height[R] > 0:
                    area += min(maxLeft, maxRight) - height[R]
                maxRight = max(maxRight, height[R])

        return area