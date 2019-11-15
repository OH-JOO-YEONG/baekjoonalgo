# 백준 기타줄
import sys

n, m = map(int, sys.stdin.readline().split())
pack, each = 1000, 1000
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    pack = min(a, pack)
    each = min(b, each)

total = 0

# 패키지가 낱개 6개보다 비싸면 패키지에 낱개 6개로 대체
if pack > each * 6:
    pack = 6 * each

if pack < (n % 6) * each: # 나머지 낱개 * 가격이 패키지보다 높으면
    total = pack * (n // 6) + pack
else: # 낮으면
    total = pack * (n // 6) + each * (n % 6)
print(total)



