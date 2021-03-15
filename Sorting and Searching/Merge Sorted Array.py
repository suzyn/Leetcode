class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Approach 1 : 44ms, 14.3 MB
        for i in range(len(nums2)):
            if(nums1[-1-i]==0):
                nums1[-1-i]=nums2[i]
        nums1.sort()
        
        
        # Approach 2 : 36ms, 14.3MB
        if n!=0:
            j=0
            for i in range(m, len(nums1)):
                nums1[i]=nums2[j]
                j+=1
            nums1.sort()
        