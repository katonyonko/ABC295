import io
import sys

_INPUT = """\
6
5
1 2 3 3
5
2 4
1 4 2
2 4
1 5 1
2 4
7
1 1 2 2 3 3
10
2 5
1 5 2
2 5
1 2 1
1 7 1
1 6 3
2 5
2 6
2 1
1 7 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import sys
  sys.setrecursionlimit(10**6)
  class UnionFind():
    def __init__(self, n):
      self.n = n
      self.parents = [-1] * n
      self.repr = [i for i in range(n)]
    def find(self, x):
      if self.parents[x] < 0:
        return x
      else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.parents[x] > self.parents[y]:
        x, y = y, x
      self.parents[x] += self.parents[y]
      self.parents[y] = x
      self.repr[x] = min(self.repr[x],self.repr[y])
    def size(self, x):
      return -self.parents[self.find(x)]
    def same(self, x, y):
      return self.find(x) == self.find(y)
    def members(self, x):
      root = self.find(x)
      return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
      return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
      return len(self.roots())
    def all_group_members(self):
      return {r: self.members(r) for r in self.roots()}
    def __str__(self):
      return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

  N=int(input())
  p=list(map(lambda x: int(x)-1, input().split()))
  uf=UnionFind(N)
  Q=int(input())
  for i in range(Q):
    query=input().split()
    if query[0]=='1':
      u,v=map(lambda x:int(x)-1,query[1:])
      while uf.find(u)!=uf.find(v):
        nxt=p[uf.repr[uf.find(u)]-1]
        uf.union(u,v)
        u=nxt
    else:
      x=int(query[1])-1
      print(uf.repr[uf.find(x)]+1)