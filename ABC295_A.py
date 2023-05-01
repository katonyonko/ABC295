import io
import sys

_INPUT = """\
6
10
in that case you should print yes and not no
10
in diesem fall sollten sie no und nicht yes ausgeben
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  W=input().split()
  ans='No'
  for i in range(N):
    if W[i] in ['and','not','that','the','you']: ans='Yes'
  print(ans)