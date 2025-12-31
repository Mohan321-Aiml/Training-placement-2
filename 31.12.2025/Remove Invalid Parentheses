class Solution:
    def removeInvalidParentheses(self, s):
        res=set()
        def dfs(s,i,l,r,bal):
            if bal<0 or l<0 or r<0:
                return
            if i==len(s):
                if bal==0:
                    res.add(s)
                return
            if s[i]=='(':
                dfs(s[:i]+s[i+1:],i,l-1,r,bal)
                dfs(s,i+1,l,r,bal+1)
            elif s[i]==')':
                dfs(s[:i]+s[i+1:],i,l,r-1,bal)
                dfs(s,i+1,l,r,bal-1)
            else:
                dfs(s,i+1,l,r,bal)
        l=r=0
        for c in s:
            if c=='(':
                l+=1
            elif c==')':
                if l==0:
                    r+=1
                else:
                    l-=1
        dfs(s,0,l,r,0)
        return list(res)
