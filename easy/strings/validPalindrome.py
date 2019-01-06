class Solution:
    def isLetter(self, c):
        """
        :type c: char
        :rtype: bool

        Returns True if alphanumeric character based on ASCII value.
        """
        return  (48 <= ord(c) <= 57) or (65 <= ord(c) <= 90) or (97 <= ord(c) <= 122)

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        S = ""
        for c in s:
            if self.isLetter(c):
                S += c.lower()

        return S == S[::-1]
