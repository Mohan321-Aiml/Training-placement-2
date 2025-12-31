class Solution:
    def findMinHeightTrees(self, n, edges):
        if n==1:
            return [0]
        g=[set() for _ in range(n)]
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)
        leaves=[i for i in range(n) if len(g[i])==1]
        while n>2:
            n-=len(leaves)
            new=[]
            for x in leaves:
                y=g[x].pop()
                g[y].remove(x)
                if len(g[y])==1:
                    new.append(y)
            leaves=new
        return leaves
