# 백준 신입사원
import sys
n = int(sys.stdin.readline())

for i in range(n):
    a = int(sys.stdin.readline())
    man = []
    for j in range(a):
        a, b = map(int, sys.stdin.readline().split())
        man.append([a, b])
    man = sorted(man, key=lambda man: man[0])
    cnt = 0
    per = 1
    for k in range(0, len(man)):
        if man[cnt][1] > man[k][1]:
            per += 1
            cnt = k
    print(per)

# for i in range(1, n):
#     if conf[i][0] >= conf[j][1]:
#         per += [conf[i]]
#         j = i