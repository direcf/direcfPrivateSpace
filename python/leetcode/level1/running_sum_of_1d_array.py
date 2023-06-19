# Runtime: 29 ms, faster than 64.54% of Python online submissions for Running Sum of 1d Array.
# Memory Usage: 13.5 MB, less than 89.28% of Python online submissions for Running Sum of 1d Array.
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        tmp = 0 # NOTE: Using a long runtime
        for i in nums:
            tmp += i
            result.append(tmp)
        return result

# NOTE: Not using 'tmp' list (Extra array takes a long runtime)
# Runtime: 15 ms, faster than 99.37% of Python online submissions for Running Sum of 1d Array.
# Memory Usage: 13.4 MB, less than 89.28% of Python online submissions for Running Sum of 1d Array.
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [nums[0]]
        for i in nums[1:]:
            result.append(result[-1] + i)
        return result