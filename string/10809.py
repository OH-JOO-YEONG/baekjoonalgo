# 백준 알파벳 찾기
from string import ascii_lowercase
S = input()

a = [[chr(97 + i), -1] for i in range(26)]

name_1 = []
for i, name in enumerate(S):
    name_1 += [[name, i]]

for i in range(26):
    for j in range(len(name_1)):
        if a[i][0] == name_1[j][0]:
            if a[i][1] >= 0 and a[i][1] < name_1[j][1]:
                pass
            else:
                a[i][1] = name_1[j][1]
for i in range(26):
    print(a[i][1], end=' ')