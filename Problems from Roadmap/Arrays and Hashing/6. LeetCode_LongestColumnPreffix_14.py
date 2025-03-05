#Steps:
#1. loop through each string in strs
#2. loop through each char in str in strs
#3. see if the chars are the same in all
#4. If yes, append it to the result string
#5. If not, return the result string
#The below approach is called vertical scanning.

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if  i == len(s) or s[i] != strs[0][i]:
                    return s[:i]

        return strs[0]