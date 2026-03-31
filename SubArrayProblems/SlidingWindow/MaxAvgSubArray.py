'''
Problem : Maximum Avg subarray
Platform : Leetcode

Basically we were asked to get the maximum average of subarray length is equals to k
We can use Fixed Sliding Window

Time Complexity : O(n)
Space Complexity : O(1)
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        (m,s)=(0,0)
        for i in range(0,k):
            s+=nums[i]
        m=s/k
        for i in range(k,len(nums)):
            j=i-k
            s+=nums[i]-nums[j]
            m=max(m,s/k)
        return m
