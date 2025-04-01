class Solution:
    def isPalindrome(self, s):
        L, R = 0, len(s) - 1 

        while L < R:
            left = s[L].lower()
            right = s[R].lower()

            if left.isalnum() and right.isalnum():
                if left != right:
                    return False
                L += 1
                R -= 1

            elif not left.isalnum():
                L += 1

            elif not right.isalnum():
                R -= 1

        return True