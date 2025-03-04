#APPROACH 1

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums , k: int):
        out = []
        hmap = defaultdict(int)

        for i in nums:
            hmap[i] += 1
        out = sorted(hmap, key=hmap.get, reverse = True)[:k]
        return out
    
        #APPROACH 2
        for n,c in hmap.items():
            freq[c].append(n)

            for i in range(len(freq)- 1, 0, -1):
                for j in freq[i]:
                    out.append(j)
                    if len(out) == k:
                        return out