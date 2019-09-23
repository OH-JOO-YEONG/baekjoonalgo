# 백준 대회 or 인턴

# 팀은 여자 2 남자 1로 이루어져있고
# M >= 2 : 여자가 2명 이상이다.
# N >= 1 : 남자가 1명 이상이다.
# M + N >= 3 + K : 남은 사람들의 수가 제외할 사람들의 수 + 한 팀 이상이다.

n, m, k = map(int, input().split())
team = 0
while n >= 2 and m >= 1 and (n + m) >= 3 + k:
    n -= 2
    m -= 1
    team += 1
print(team)

