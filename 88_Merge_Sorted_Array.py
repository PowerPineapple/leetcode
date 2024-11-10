class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if n < 1:
            exit
        else:
            j=0
            i=0
            for i in range(m+n):
                if j < n and nums1[i] >= nums2[j]:
                    nums1.insert(i, nums2[j])
                    j=j+1
                    nums1.pop()
                elif n+m > i >= m+j and j < n and nums1[i] == 0:
                    nums1[i]=nums2[j]
                    j=j+1
                    
            
