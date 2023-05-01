import io
import sys

_INPUT = """\
6
20230322
0112223333444445555556666666777777778888888889999999999
3141592653589793238462643383279502884197169399375105820974944
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  ans=0
  tmp=[0]*(2**10)
  tmp[0]+=1
  now=0
  for i in range(len(S)):
    now^=1<<int(S[i])
    tmp[now]+=1
  for i in range(2**10):
    ans+=tmp[i]*(tmp[i]-1)//2
  print(ans)