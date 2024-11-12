class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        way = [100000 for i in nums]
        way[0] = 0
        for i in range(l-1):
            z = nums[i] if nums[i]+i < l else l - i - 1
            for j in range(1, z+1):
                if way[i+j] > way[i] + 1:
                    way[i+j] = way[i] + 1
        return way[l-1]
