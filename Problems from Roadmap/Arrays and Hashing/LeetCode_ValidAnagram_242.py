class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Thashmap = {}
        Shashmap = {}

        for i in s:
            if i not in Shashmap:
                Shashmap[i] = 1
            else:
                Shashmap[i] += 1
        for j in t:
            if j not in Thashmap:
                Thashmap[j] = 1
            else:
                Thashmap[j] += 1
        return Shashmap == Thashmap