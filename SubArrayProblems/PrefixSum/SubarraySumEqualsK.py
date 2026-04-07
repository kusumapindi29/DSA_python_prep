'''
Problem: Subarray Sum Equals K
Platform: LeetCode

Since the array may contain negative numbers, the sliding window (two pointer) 
approach does NOT work reliably.

Instead, we use Prefix Sum + HashMap.

We maintain a running prefix sum. At each index:
- If (sum - k) exists in the hashmap, it means there is a subarray 
  ending at the current index whose sum is k.

Why?
Because:
    sum - previous_prefix_sum = k
→ So removing the previous prefix gives a subarray of sum k.

We store prefix sums in a hashmap along with their frequencies to count 
all such subarrays efficiently.
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h={}    # to store prefix sum
        h[0]=1  # basically we add the prefix of the array as zero
        s=0     # sum of the number
        r=0     # number of subarray whose sum equals k
        for i in range(0,len(nums)):
            s+=nums[i]
            if (s-k) in h:
                r+=h[s-k]
            if s in h:
                h[s]+=1
            else:
                h[s]=1
        return r

