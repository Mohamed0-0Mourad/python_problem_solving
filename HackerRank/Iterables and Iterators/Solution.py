# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
a = input().split()
r = int(input())

comb = combinations(a, r)

cnt = 0
num_comb = 0
i=0
for t in comb:
    num_comb +=1
    try:
        i = t.index('a')
        cnt+=1
    except ValueError:
        continue

print(cnt / num_comb)
