class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c in mapping:
                if not stack:
                    return False
                last = stack.pop()
                if last != mapping[c]:
                    return False
            else:
                stack.append(c)

        return not stack