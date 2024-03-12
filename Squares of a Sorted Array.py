class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = (num*num for num in nums)
        ans = sorted(ans)
        return ans