import io
import sys

_INPUT = """\
6
6
4 1 7 4 1 4
1
158260522
10
295 2 29 295 29 2 29 295 2 29
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N=int(input())
  A=list(map(int,input().split()))
  d=defaultdict(int)
  for i in range(N):
    d[A[i]]+=1
  ans=0
  for key in d:
    ans+=d[key]//2
  print(ans)