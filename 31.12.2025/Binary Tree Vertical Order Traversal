class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        from collections import defaultdict,deque
        d=defaultdict(list)
        q=deque([(root,0)])
        while q:
            n,c=q.popleft()
            d[c].append(n.val)
            if n.left:
                q.append((n.left,c-1))
            if n.right:
                q.append((n.right,c+1))
        return [d[x] for x in sorted(d)]
