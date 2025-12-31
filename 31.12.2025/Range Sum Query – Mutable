  class NumArray:
    def __init__(self, nums):
        self.n=len(nums)
        self.bit=[0]*(self.n+1)
        self.arr=nums[:]
        for i,x in enumerate(nums):
            j=i+1
            while j<=self.n:
                self.bit[j]+=x
                j+=j&-j
    def update(self, i, val):
        d=val-self.arr[i]
        self.arr[i]=val
        j=i+1
        while j<=self.n:
            self.bit[j]+=d
            j+=j&-j
    def sumRange(self, l, r):
        def s(i):
            t=0
            i+=1
            while i>0:
                t+=self.bit[i]
                i-=i&-i
            return t
        return s(r)-s(l-
