class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if  i == len(s) or s[i] != strs[0][i]:
        #             return s[:i]

        # return strs[0]

        result = str(strs[0])
        for i in range(len(strs)):
            j = 0
            while j < min(len(result), len(strs[i])):
                if result != strs[i][j]:
                    break
                j += 1
        return result