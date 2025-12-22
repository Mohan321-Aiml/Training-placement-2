class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr=encoding

    def next(self, n: int) -> int:
        ans=-1
        while self.arr:
            limit=self.arr[0]
            if limit>n:
                self.arr[0]=limit-n
                ans=self.arr[1]
                break
                
            elif limit==n:
                ans=self.arr[1]
                self.arr=self.arr[2:]
                break
            else:
                if self.arr:
                    n-=self.arr[0]
                    self.arr=self.arr[2:]
                else:
                    return -1
        return ans


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
