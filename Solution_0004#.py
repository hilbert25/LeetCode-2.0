class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l%2 == 1:
            return self.findK(nums1,nums2,l/2+1)
        else:
            return (self.findK(nums1,nums2,l/2)+self.findK(nums1,nums2,l/2+1))/2
    def findK(self,nums1,nums2,k):
        if len(nums1) > len(nums2):
            #如果长的在前边可能导致短的越界，看后边前一个数组搜索范围不会大于k/2，因此后边的不会小于k/2，后边的需要长一点
            return self.findK(nums2, nums1, k)
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0],nums2[0])
        a = int(min(len(nums1),k/2))#每个都搜k/2
        b = int(k - a)
        if nums1[a-1] <= nums2[b-1]:
            return self.findK(nums1[a:],nums2,b)
        else:
            return self.findK(nums1,nums2[b:],a)
s = Solution()
print s.findMedianSortedArrays([1,3],[2])