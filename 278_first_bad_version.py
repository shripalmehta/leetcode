# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

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
        low = 0
        high = n
        while (low<high):
            mid = low+(high-low)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid+1
        return low
        
        
        # Alternate Solution:
        """        
        def getFirstBadVersion(low, high, x):
            
            if (high-low <= 1):
                if isBadVersion(low):
                    return low
                elif isBadVersion(x-1):
                    return x-1
                elif isBadVersion(x):
                    return x
            
            mid = (low+high)//2
            if isBadVersion(mid):
                return getFirstBadVersion(low, mid-1, mid)
            else:
                return getFirstBadVersion(mid+1, high, high)
            
        return getFirstBadVersion(1, n, n)
        """