# 백준 로프문제

import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    b = int(sys.stdin.readline())
    a.append(b)
a.sort()
max = 0

for i in range(n, 0, -1):
    a[i - 1] = a[i - 1] * (n + 1 - i)
    if max < a[i - 1]:
        max = a[i - 1]
print(max)
