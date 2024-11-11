class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = 0
        for i in range(len(nums)):
            if d >= i:
                d = max(d, i+nums[i])
            else:
                return bool(0)
        return bool(1)
