class Solution:
    def minEatingSpeed(self, piles, h):
        L, R = 1, max(piles)
        res = 0
        
        if len(piles) == h:
            return R

        while L <= R:
            k = L + (R - L) // 2 # Avoid integer overflowing

            total = 0
            for p in piles:
                total += math.ceil(p / k)
            
            if total > h:
                L = k + 1
            else:
                res = k
                R = k - 1
        return res