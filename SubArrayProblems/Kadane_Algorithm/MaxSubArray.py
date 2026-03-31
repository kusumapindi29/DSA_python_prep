'''
Problem : Maximum sub array
Platform : Leetcode
Algorithm : kadane's

Kadane's Algorithm:
At each step, decide whether to start a new subarray
or extend the current one.

Time Complexity: O(n)
Space Complexity : O(1)
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c=nums[0] # To track current sum
        m=nums[0] # To track max sum
        for i in range(1,len(nums)):
            c=max(nums[i],nums[i]+c)
            m=max(m,c)
        return m
