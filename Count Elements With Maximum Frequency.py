class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = {}
        for num in nums:
            ans[num] = ans.get(num, 0) + 1

        count = 0
        max_freq = float('-inf')
        for freq in ans.values():
            max_freq = max(max_freq, freq)

        for freq in ans.values():
            if freq == max_freq:
                count += max_freq

        return count
        