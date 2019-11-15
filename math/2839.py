# 백준 설탕배달

import sys

n = int(sys.stdin.readline())

sweet = 0
while True:
    if n % 5 == 0:
        sweet += n // 5
        print(sweet)
        break
    n = n - 3
    sweet += 1

    if n < 0:
        print(-1)
        break


