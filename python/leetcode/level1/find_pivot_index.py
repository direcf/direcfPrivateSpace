# Runtime: 130 ms, faster than 65.17% of Python online submissions for Find Pivot Index.
# Memory Usage: 14.3 MB, less than 97.02% of Python online submissions for Find Pivot Index.
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return 0
        
        left = 0
        right = sum(nums)
        
        for i in range(length):
            if i == 0:
                pass
            else:
                left += nums[i-1] 
            right -= nums[i]
            
            # check pivot existence
            if left == right:
                return i
            
        return -1

# NOTE: Leetcode solution
# Runtime: 123 ms, faster than 70.88% of Python online submissions for Find Pivot Index.
# Memory Usage: 14.6 MB, less than 43.90% of Python online submissions for Find Pivot Index.
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1