class Solution:
    def maxProfit(self, prices):
        hold=sold=rest=0
        hold=-10**9
        for p in prices:
            hold=max(hold,rest-p)
            rest=max(rest,sold)
            sold=hold+p
        return max(sold,rest)
