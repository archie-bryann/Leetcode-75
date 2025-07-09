from collections import Counter


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums_hash = {}

        for num in nums:
            if num in nums_hash:
                # no need to add 1
                return True
            else:
                nums_hash[num] = 1

        return False




