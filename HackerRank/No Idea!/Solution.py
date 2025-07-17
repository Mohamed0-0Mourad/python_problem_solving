# Enter your code here. Read input from STDIN. Print output to STDOUT

sizes = list(map(int, input().split())) 
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))



res = 0
for num in arr:
    if num in A: # Takes O(1) average for a set is implemented as hash tables
        res+=1
    elif num in B:
        res-=1

print(res)
