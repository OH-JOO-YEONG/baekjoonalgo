# 백준 ATM

n = int(input())
a = list(map(int, input().split()))
a.sort()
sum = 0
line = 0
for i in range(n):
    sum = a[i] + sum
    line = sum + line
print(line)