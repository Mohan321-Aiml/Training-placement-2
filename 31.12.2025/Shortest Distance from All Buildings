class Solution:
    def shortestDistance(self, grid):
        from collections import deque
        m,n=len(grid),len(grid[0])
        dist=[[0]*n for _ in range(m)]
        reach=[[0]*n for _ in range(m)]
        buildings=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    buildings+=1
                    q=deque([(i,j,0)])
                    seen=[[False]*n for _ in range(m)]
                    seen[i][j]=True
                    while q:
                        x,y,d=q.popleft()
                        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<m and 0<=ny<n and not seen[nx][ny] and grid[nx][ny]==0:
                                seen[nx][ny]=True
                                dist[nx][ny]+=d+1
                                reach[nx][ny]+=1
                                q.append((nx,ny,d+1))
        ans=10**9
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and reach[i][j]==buildings:
                    ans=min(ans,dist[i][j])
        return ans if ans<10**9 else
