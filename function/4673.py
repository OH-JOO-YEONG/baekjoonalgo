# 백준 셀프넘버

dn = [0 for i in range(100001)]
def d(n):
    sum = n

    while True:
        if n == 0:
            break
        sum += n % 10
        n = n // 10
    return sum

for i in range(1, 10001):
    dn[d(i)] = 1
    if dn[i] == 0:
        print(i)
