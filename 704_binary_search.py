# 704. Binary Search 
# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(low, high, nums, target):
            if low > high:
                return -1
            mid = (low + high)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                return binary_search(mid+1, high, nums, target)
            else:
                return binary_search(low, mid-1, nums, target)
        
        return binary_search(0, len(nums)-1, nums, target)

