# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

a = list(map(int,input().split()))
s = sum(a)
cur = ans = sum(a[i] * (i + 1) for i in range(n))
for i in range(n):
    cur = cur - s + a[i] * n
    ans = max(ans,cur)
    
print(ans)
