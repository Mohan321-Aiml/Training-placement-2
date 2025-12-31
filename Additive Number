class Solution:
    def isAdditiveNumber(self, num):
        n=len(num)
        for i in range(1,n):
            for j in range(i+1,n):
                a,b=num[:i],num[i:j]
                if (a[0]=='0' and len(a)>1) or (b[0]=='0' and len(b)>1):
                    continue
                x,y=int(a),int(b)
                k=j
                while k<n:
                    z=x+y
                    s=str(z)
                    if not num.startswith(s,k):
                        break
                    k+=len(s)
                    x,y=y,z
                if k==n:
                    return True
        return False
