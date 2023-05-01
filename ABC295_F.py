import io
import sys

_INPUT = """\
6
6
22 23 234
0295 295 295
0 1 9999999999999999
2718 998244353 9982443530000000
869120 1234567890123456 2345678901234567
2023032520230325 1 9999999999999999
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  T=int(input())
  for _ in range(T):
    S,L,R=input().split()
    L,R=int(L),int(R)
    def func(x,s):
      if x==0: return 0
      n=len(s)
      res=0
      if s[0]=='0': flg=0
      else: flg=1
      s=int(s)
      for i in range(16-n+1):
        before=x//(10**(16-i))
        mid=(x-before*(10**(16-i)))//(10**(16-i-n))
        after=x%(10**(16-i-n))
        if flg==0:
          if before>0: res+=(before-1)*(10**(16-i-n))
        else: res+=before*(10**(16-i-n))
        if mid>s:
          if flg==0 and before>0 or flg==1: res+=10**(16-i-n)
        elif mid==s:
          if flg==0 and before>0 or flg==1: res+=after+1
      return res
    print(func(R,S)-func(L-1,S))