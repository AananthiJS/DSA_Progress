class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        #L, R = 0 , 0

        #for L in range(len(nums)):
        #    for R in range(L + 1, min(len(nums), L + k + 1)):
        #        if nums[L] == nums[R]:
        #            return True
        #return False
        seen = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                seen.remove(nums[l])
                l += 1
            if nums[r] in seen:
                return True
            seen.add(nums[r])
        return False