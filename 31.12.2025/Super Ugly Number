class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly=[1]
        idx=[0]*len(primes)
        while len(ugly)<n:
            vals=[primes[i]*ugly[idx[i]] for i in range(len(primes))]
            m=min(vals)
            ugly.append(m)
            for i in range(len(primes)):
                if vals[i]==m:
                    idx[i]+=1
        return ugly[-1]
