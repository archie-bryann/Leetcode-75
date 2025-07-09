class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_hash = {} # number : i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_hash:
                return [nums_hash[complement], i]
            nums_hash[num] = i