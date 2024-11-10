class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        i = 0
        n = len(nums)
        wrongs = []
        while cnt <= n/2:
            if wrongs.count(nums[i]) == 0:
                cnt = nums.count(nums[i])
                wrongs = wrongs + [nums[i]]
            i = i + 1
        return nums[i-1]
