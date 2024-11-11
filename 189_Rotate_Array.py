class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        tst = nums[l-k:] + nums[:l-k]
        for i in range(l):
            nums[i] = tst[i]
