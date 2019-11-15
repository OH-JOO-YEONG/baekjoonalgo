# 백준 문자열 반복
import sys

n = int(sys.stdin.readline())

for i in range(n):
    string = ""
    a, b = sys.stdin.readline().split()
    a = int(a)
    for j in b:
        string += j * a
    print(string)