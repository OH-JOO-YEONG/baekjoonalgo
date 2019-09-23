# 백준 동전 0

n, k = map(int, input().split())
coin = []
count_sum = 0
for i in range(n):
    a = int(input())
    coin.append(a)

for i in range(len(coin), 0, -1):
    count = k // coin[i - 1]
    k -= coin[i - 1] * count
    count_sum += count
    if k == 0:
        break

print(count_sum)