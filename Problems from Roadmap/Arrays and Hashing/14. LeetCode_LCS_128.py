class Solution:
    def longestConsecutive(self, nums):
        hashset = (set(nums))
        length = 0

        for i in hashset:
            if i - 1 not in hashset:
                count = 1
                while i + count in hashset:
                    count += 1
                length = max(count, length)

        return length