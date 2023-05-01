import io
import sys

_INPUT = """\
6
4 4
.1.#
###.
.#2.
#.##
2 5
..#.#
###.#
2 3
11#
###
4 6
#.#3#.
###.#.
##.###
#1..#.
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  R,C=map(int,input().split())
  B=[input() for _ in range(R)]
  ans=[]
  for i in range(R):
    for j in range(C):
      res='#'
      if B[i][j]=='.': res='.'
      for k in range(R):
        for l in range(C):
          if B[k][l] not in ['#','.'] and abs(i-k)+abs(j-l)<=int(B[k][l]): res='.'
      ans.append(res)
  for i in range(R):
    print(*ans[C*i:C*(i+1)],sep='')