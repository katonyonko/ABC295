import io
import sys

_INPUT = """\
6
3 5 2
2 0 4
2 3 1
0 0
10 20 7
6 5 0 2 0 0 0 15 0 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import accumulate
  mod=998244353
  N,M,K=map(int,input().split())
  A=sorted(list(map(int,input().split())))
  zeros=A.count(0)
  cnt=[0]*(M+1)
  for i in range(N-zeros):
    cnt[A[i+zeros]]+=1
  cnt=list(accumulate(cnt))
  m=pow(M,mod-2,mod)
  F=[1]
  for i in range(N):
    F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(N):
    I.append(I[-1]*(N-i)%mod)
  I=I[::-1]

  def AF(x,y):
    '''
    zeros個の項の中でx未満のものの数がy個未満である確率を返す
    '''
    global zeros
    global M
    z,w=(x-1)*m%mod,(M-x+1)*m%mod
    res=0
    y=min(y,zeros+1)
    for i in range(y):
      res+=F[zeros]*I[i]*I[zeros-i]*pow(z,i,mod)*pow(w,zeros-i,mod)
      res%=mod
    return res

  ans=0
  for i in range(M):
    if K-cnt[i]<0: continue
    x=i+1
    ans+=AF(x,K-cnt[i])
    ans%=mod
  print(ans)