class Solution:
    def countSmaller(self, nums):
        import bisect
        a=[]
        r=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            j=bisect.bisect_left(a,nums[i])
            r[i]=j
            a.insert(j,nums[i])
        return r
