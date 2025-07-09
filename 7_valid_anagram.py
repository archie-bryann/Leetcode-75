class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) === sorted(t)
        if len(s) != len(t):
            return False

        hash = {}

        for char in s:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

        for char in t:
            if char not in hash:
                return False
            hash[char] -= 1

            if hash[char] < 0:
                return False

        return True