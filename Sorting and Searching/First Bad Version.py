# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach1 : Binary Search (24ms, 13.9MB)
        left=1
        right=n
        
        while(left<right):
            mid=(left+right)//2
            if isBadVersion(mid):right=mid
            else:left=mid+1                 # isBadVersion(mid)==False
        return left
    
        