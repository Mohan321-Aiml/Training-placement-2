class Solution:
    def lengthOfLIS(self, nums):
        dp=[]
        import bisect
        for x in nums:
            i=bisect.bisect_left(dp,x)
            if i<len(dp):
                dp[i]=x
            else:
                dp.append(x)
        return len(dp)
