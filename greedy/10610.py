# 백준 30

n = input()
count = 0
sum = 0
for i in n:
    if i == '0':
        count += 1
    else:
        sum += int(i)
if count == 0:
    print(-1)
else:
    if sum % 3 == 0:
        n = list(map(int, sorted(n)))
        for i in range(len(n) - 1, -1, -1):
            print(n[i], end='')
    else:
        print(-1)
