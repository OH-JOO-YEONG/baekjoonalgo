# 백준 회의실배정

import sys
n = int(sys.stdin.readline())
conf = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    conf.append((a, b))
conf = sorted(conf, key=lambda time: time[0])
conf = sorted(conf, key=lambda time: time[1])
per = []
per.append(conf[0])
j = 0
for i in range(1, n):
    if conf[i][0] >= conf[j][1]:
        per += [conf[i]]
        j = i
print(len(per))

