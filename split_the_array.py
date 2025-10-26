class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        count = Counter(nums)
        
        for val in count.values():
            if val > 2:
                return False
        return True
    